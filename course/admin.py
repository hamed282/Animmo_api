from django.contrib import admin
from .models import CourseCategoryModel, CourseSubCategoryModel, CourseModel, SampleExerciseModel, OrderModel,\
    OrderItemModel


admin.site.register(CourseCategoryModel)
admin.site.register(CourseSubCategoryModel)
admin.site.register(CourseModel)
admin.site.register(SampleExerciseModel)
admin.site.register(OrderModel)
admin.site.register(OrderItemModel)
