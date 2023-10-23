from django.contrib import admin
from .models import CourseModel, CourseCategoryModel


admin.site.register(CourseCategoryModel)
admin.site.register(CourseModel)
