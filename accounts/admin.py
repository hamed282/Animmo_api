from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserCreationForm, UserChangeForm
from .models import User, OtpCode


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['first_name', 'last_name', 'phone_number']
    list_filter = ['is_active']

    readonly_fields = ['last_login']

    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'phone_number', 'deaf', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'phone_number')}),
    )

    search_fields = ['phone_number', 'first_name', 'last_name']
    ordering = ['first_name', 'last_name']

    filter_horizontal = ()


class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'created']


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

admin.site.register(OtpCode, OtpCodeAdmin)




