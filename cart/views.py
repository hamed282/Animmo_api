from rest_framework.views import APIView
from .service import Cart
from rest_framework.response import Response
from rest_framework import status


class CartAPI(APIView):

    def get(self, request, format=None):
        cart = Cart(request)

        return Response(
            {"data": list(cart.__iter__()),
             "cart_total_price": cart.get_total_price()},
            status=status.HTTP_200_OK
            )

    def post(self, request, **kwargs):
        """
        parameters:
        1. id # course id
        2. price # course price
        3. remove # true or false
        4. clear # true or false

        """
        cart = Cart(request)
        if request.data["remove"] == 'true':
            product = request.data["id"]
            cart.remove(product)

        elif request.data["clear"] == 'true':
            cart.clear()

        else:
            product_id = request.data["id"]
            price = request.data["price"]
            cart.add(
                    product_id=product_id,
                    price=price
                )

        return Response(
            {"message": "cart updated"},
            status=status.HTTP_202_ACCEPTED)
