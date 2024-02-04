from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSerializer, OrderItemSerializer
from .models import OrderModel, OrderItemModel, CourseModel
from rest_framework_simplejwt.authentication import JWTAuthentication


class AddCartView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        """
        parameters:
        1. course
        2. price
        """
        form = request.data
        ser_data = OrderItemSerializer(data=form)
        print('##########################################')
        if ser_data.is_valid():
            print('----------------------------------------')

            paid_check = OrderModel.objects.filter(user=request.user, paid=False).exists()
            if not paid_check:
                OrderModel.objects.create(user=request.user)

            course = CourseModel.objects.get(course=ser_data.validated_data['course'])
            exist_course = OrderItemModel.objects.filter(course=course).exists()
            if not exist_course:
                price = ser_data.validated_data['price']
                order = OrderModel.objects.get(user=request.user)
                OrderItemModel.objects.create(order=order, course=course, price=price)
            else:
                pass
        order = OrderModel.objects.get(user=request.user, paid=False)
        orders = OrderItemModel.objects.filter(order=order).all()

        ser_order = OrderItemSerializer(instance=orders, many=True)

        return Response(data=(ser_order.data, {'total_price': order.get_total_price()}))
