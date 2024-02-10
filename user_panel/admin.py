from django.contrib import admin
from .models import UserCourseModel


class UserCourseAdmin(admin.ModelAdmin):
    list_display = ['user', 'course']


admin.site.register(UserCourseModel, UserCourseAdmin)
