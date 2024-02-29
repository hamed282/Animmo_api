
from decimal import Decimal

from django.conf import settings

from course.serializers import CourseSerializer
from course.models import CourseModel


class Cart:
    def __init__(self, request):
        """
        initialize the cart
        """
        self.session = request.session
        print('----------------')
        print(request.session.session_key)

        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        self.session.modified = True

    def add(self, product_id, price):
        """
        Add product to the cart or update its quantity
        """

        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": 0,
                "price": str(price)
            }

        self.cart[product_id]["quantity"] = 1

        self.save()

    def remove(self, product_id):
        """
        Remove a product from the cart
        """

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Loop through cart items and fetch the products from the database
        """
        product_ids = self.cart.keys()
        products = CourseModel.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]["product"] = CourseSerializer(product).data
        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        """
        Count all items in the cart
        """
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item["price"]) * item["quantity"] for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()
