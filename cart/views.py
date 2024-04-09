from rest_framework.views import APIView
from .service import Cart
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from . models import OrderModel, OrderItemModel, DiscountModel
from user_panel.models import UserCourseModel
from course.models import CourseModel
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
import json
import requests
from rest_framework import status


# class CartAPI(APIView):
#
#     def get(self, request, format=None):
#         cart = Cart(request)
#
#         return Response(
#             {"data": list(cart.__iter__()),
#              "cart_total_price": cart.get_total_price()},
#             status=status.HTTP_200_OK
#             )
#
#     def post(self, request, **kwargs):
#         """
#         parameters:
#         1. id # course id
#         2. price # course price
#         3. remove # true or false
#         4. clear # true or false
#
#         sample json:
#
#         {
#             "id": "2",
#             "price":"300000",
#             "remove":"false",
#             "clear":"true"
#         }
#         """
#         cart = Cart(request)
#         if request.data["remove"] == 'true':
#             product = request.data["id"]
#             cart.remove(product)
#
#         elif request.data["clear"] == 'true':
#             cart.clear()
#
#         else:
#             product_id = request.data["id"]
#             price = request.data["price"]
#             cart.add(
#                     product_id=product_id,
#                     price=price
#                 )
#
#         return Response(
#             {"message": "cart updated"},
#             status=status.HTTP_202_ACCEPTED)


class CartPayView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        parameters:
        1. course_id # course id


        sample json:

       {
       "course": [
                {"course_id": "1"} , {"course_id": "2"}
                 ],
       "referral_code": "ASDF"
       }
        """
        forms = request.data
        if len(forms) > 0:

            order = OrderModel.objects.create(user=request.user)
            try:
                discount_object = DiscountModel.objects.get(referral_code=forms['referral_code'])
                discount = discount_object.discount_percent
                discount_object.delete()

            except:
                discount = 0

            quantity = 1
            for form in forms['course']:
                course = CourseModel.objects.get(id=form['course_id'])
                price = course.get_off_price()
                OrderItemModel.objects.create(order=order, course=course, price=price, quantity=quantity)

            ############################################

            amount = str(int(order.get_total_price()) - int(order.get_total_price()) * (int(discount)/100))

            print(amount)
            description = f' خرید دوره '
            phone = request.user.phone_number

            data = {
                "MerchantID": settings.MERCHANT,
                "Amount": amount,
                "Description": description,
                "Phone": phone,
                "CallbackURL": settings.CALLBACK_URL,
            }

            data = json.dumps(data)
            headers = {'content-type': 'application/json', 'content-length': str(len(data))}
            response = requests.post(settings.ZP_API_REQUEST, data=data, headers=headers, timeout=10)

            if response.status_code == 200:
                response = response.json()
                if response['Status'] == 100:
                    url = f"{settings.ZP_API_STARTPAY}{response['Authority']}"
                    order.authority = response['Authority']
                    order.save()
                    return Response({'redirect to : ': url}, status=200)
                else:
                    return Response({'Error code: ': 400}, status=400)
            else:
                return Response({'details': str(response.json()['errors'])})


class CartPayVerify(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):

        if request.GET.get('Status') == 'OK':

            authority = request.GET.get('Authority')
            try:
                order = OrderModel.objects.get(authority=authority)
                user = order.user
            except:
                return Response({'details': 'Authority Code not found'}, status=status.HTTP_401_UNAUTHORIZED)

            amount = order.get_total_price()

            authority = request.GET['Authority']

            data = {
                "MerchantID": settings.MERCHANT,
                "Amount": amount,
                "Authority": authority,
            }

            data = json.dumps(data)
            headers = {'content-type': 'application/json', 'content-length': str(len(data))}
            response = requests.post(settings.ZP_API_VERIFY, data=data, headers=headers)

            if response.status_code == 200:
                response = response.json()
                if response['Status'] == 100:
                    order.status = response['Status']
                    order.ref_id = response['RefID']
                    order.paid = True
                    order.save()
                    order_items = order.items.all()

                    for item in order_items:
                        try:
                            course = item.course
                            price = course.get_off_price()

                            phone_number = user.phone_number
                            spotplayer_license = course.spot_player_license

                            # Spotplayer
                            headers = {'$API': settings.API_KEY,
                                       '$LEVEL': '-1',
                                       }
                            data = {
                                "course": f"{spotplayer_license}",
                                "name": f"{phone_number}",
                                "watermark": {"texts": [{"text": f"{phone_number}"}]}
                            }
                            # sending post request and saving response as response object
                            r = requests.post(url=settings.API_ENDPOINT, headers=headers, json=data)
                            spot_json = r.json()
                            spotplayer_license = spot_json['key']
                        except:
                            course = item.course
                            price = course.get_off_price()

                            spotplayer_license = 'Wait'

                        UserCourseModel.objects.create(user=user, course=course,
                                                       spotplayer_license=spotplayer_license, price=price)

                    # return Response({'details': 'Transaction success'}, status=status.HTTP_200_OK)
                    return HttpResponseRedirect(redirect_to='https://animmo.ir/userProfile/')
                else:
                    # return Response({'details': 'Transaction failed or canceled by user'}, status=response.Status)
                    return HttpResponseRedirect(redirect_to='https://animmo.ir/userProfile/')
            else:
                # return Response({'details': 'Transaction failed or canceled by user'}, status=status.HTTP_406_NOT_ACCEPTABLE)
                return HttpResponseRedirect(redirect_to='https://animmo.ir/userProfile/')
        else:
            # return Response({'details': 'Transaction failed or canceled by user'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            return HttpResponseRedirect(redirect_to='https://animmo.ir/userProfile/')

