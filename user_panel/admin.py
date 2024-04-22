from django.contrib import admin
from .models import UserCourseModel


class UserCourseAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'spotplayer_license']


admin.site.register(UserCourseModel, UserCourseAdmin)
