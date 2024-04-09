from django.contrib import admin
from .models import OrderModel, OrderItemModel, DiscountModel


class OrderItemInline(admin.TabularInline):
    model = OrderItemModel
    # raw_id_fields = ('course',)


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'updated', 'paid')
    list_filter = ('paid',)
    inlines = (OrderItemInline, )


class DiscountModelAdmin(admin.ModelAdmin):
    list_display = ['referral', 'referral_code', 'discount_percent', 'discount_amount', 'active']


admin.site.register(DiscountModel, DiscountModelAdmin)
