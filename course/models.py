from django.db import models
from accounts.models import User


class CourseCategoryModel(models.Model):
    category = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='images/icon/category/')
    class_des = models.CharField(max_length=20, default='course_category')


class CourseSubCategoryModel(models.Model):
    category = models.ForeignKey(CourseCategoryModel, on_delete=models.CASCADE, related_name='category_subcategory')
    subcategory = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='images/course/')
    class_des = models.CharField(max_length=20, default='course_subcategory')


class CourseModel(models.Model):

    category = models.ForeignKey(CourseCategoryModel, on_delete=models.CASCADE, related_name='category_course')
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
    class_des = models.CharField(max_length=20, default='course')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.course)


class SampleExerciseModel(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_sample')
    category = models.ForeignKey(CourseCategoryModel, on_delete=models.CASCADE, related_name='category_sample')
    subcategory = models.ForeignKey(CourseSubCategoryModel, on_delete=models.CASCADE, related_name='subcategory_sample')
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name='course_sample')
    sample_exercise = models.FileField(upload_to='video/sample/')
    created = models.DateTimeField(auto_now=True)
    class_des = models.CharField(max_length=20, default='sample_exercise')


class OrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_order')
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name='course_order')
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class_des = models.CharField(max_length=20, default='order')

    def __str__(self):
        return f'{self.user} - {str(self.id)}'

    def get_total_price(self):
        total = sum(item.get_cost() for item in self.items_order.all())

        return total


class OrderItemModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='items_order')
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name='items_course')
    price = models.IntegerField()
    class_des = models.CharField(max_length=20, default='order_item')

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price
