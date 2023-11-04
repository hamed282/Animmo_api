from django.db import models
from accounts.models import User


class CourseCategoryModel(models.Model):
    category = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='images/icon/category/')


class CourseSubCategoryModel(models.Model):
    category = models.ForeignKey(CourseCategoryModel, on_delete=models.CASCADE, related_name='category_subcategory')
    subcategory = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='images/course/')


class CourseModel(models.Model):

    category = models.ForeignKey(CourseSubCategoryModel, on_delete=models.CASCADE, related_name='category_course')
    subcategory = models.ForeignKey(CourseSubCategoryModel, on_delete=models.CASCADE, related_name='subcategory_course')
    course = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='images/course/')
    # intro = models.FileField(upload_to='video/course/')
    spot_player_license = models.CharField(max_length=512)
    is_active = models.BooleanField(default=False)
    price = models.IntegerField()
    teacher = models.CharField(max_length=100)
    discount = models.IntegerField()
    season = models.IntegerField()
    duration = models.CharField(max_length=100)


class SampleExerciseModel(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_sample')
    category = models.ForeignKey(CourseCategoryModel, on_delete=models.CASCADE, related_name='category_sample')
    subcategory = models.ForeignKey(CourseSubCategoryModel, on_delete=models.CASCADE, related_name='subcategory_sample')
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name='course_sample')
    sample_exercise = models.FileField(upload_to='video/sample/')
    created = models.DateTimeField(auto_now=True)
