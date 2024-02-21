from django.contrib import admin
from .models import CourseCategoryModel, CourseSubCategoryModel, CourseModel, SampleExerciseModel, OrderModel,\
    OrderItemModel


class CourseCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


class CourseSubCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]
    list_display = ['course', 'category', 'subcategory']


admin.site.register(CourseCategoryModel, CourseCategoryAdmin)
admin.site.register(CourseSubCategoryModel, CourseSubCategoryAdmin)
admin.site.register(CourseModel, CourseAdmin)
admin.site.register(SampleExerciseModel)
admin.site.register(OrderModel)
admin.site.register(OrderItemModel)
