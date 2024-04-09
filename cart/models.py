from django.db import models
from accounts.models import User
from course.models import CourseModel


class OrderModel(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    authority = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    ref_id = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ('paid', '-updated')

    def __str__(self):
        return f'{self.user} - {self.id}'

    def get_total_price(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItemModel(models.Model):
    objects = None
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='items')
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity


class DiscountModel(models.Model):
    objects = None
    referral = models.CharField(max_length=100)
    referral_code = models.CharField(max_length=50, unique=True)
    discount_percent = models.CharField(max_length=20, blank=True, null=True)
    discount_amount = models.CharField(max_length=20, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.referral