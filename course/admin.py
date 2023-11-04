from django.contrib import admin
from .models import CourseCategoryModel, CourseSubCategoryModel, CourseModel, SampleExerciseModel


admin.site.register(CourseCategoryModel)
admin.site.register(CourseSubCategoryModel)
admin.site.register(CourseModel)
admin.site.register(SampleExerciseModel)
