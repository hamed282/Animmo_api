from django.contrib import admin
from .models import OrderModel, OrderItemModel


class OrderItemInline(admin.TabularInline):
    model = OrderItemModel
    # raw_id_fields = ('course',)


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'updated', 'paid')
    list_filter = ('paid',)
    inlines = (OrderItemInline, )

