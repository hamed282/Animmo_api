from django.db import models
from accounts.models import User
from django.utils.text import slugify


class CourseCategoryModel(models.Model):
    objects = None
    category = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    icon = models.FileField(upload_to='images/icon/category/')
    hovered_icon = models.FileField(upload_to='images/icon/category/')

    def save(self, **kwargs):
        self.slug = slugify(self.category, allow_unicode=True)
        super(CourseCategoryModel, self).save(**kwargs)

    def __str__(self):
        return f'{self.slug}'


class CourseSubCategoryModel(models.Model):
    objects = None
    category = models.ForeignKey(CourseCategoryModel, on_delete=models.CASCADE, related_name='category_subcategory')
    subcategory = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='images/course/')

    def save(self, **kwargs):
        self.slug = slugify(f'{self.subcategory} {self.category}', allow_unicode=True)
        super(CourseSubCategoryModel, self).save(**kwargs)

    def __str__(self):
        return self.slug


class CourseModel(models.Model):

    objects = None
    category = models.ForeignKey(CourseCategoryModel, on_delete=models.CASCADE, related_name='category_course')
    subcategory = models.ForeignKey(CourseSubCategoryModel, on_delete=models.CASCADE, related_name='subcategory_course')
    course = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='images/course/')
    intro = models.FileField(upload_to='video/course/intro/')
    spot_player_license = models.CharField(max_length=512)
    is_active = models.BooleanField(default=False)
    price = models.IntegerField()
    percent_discount = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    contacts_course = models.TextField()
    target_course = models.TextField()
    teacher = models.CharField(max_length=100)
    discount = models.IntegerField()
    season = models.IntegerField()
    duration = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, **kwargs):
        self.slug = slugify(f'{self.subcategory} {self.category} {self.course}', allow_unicode=True)
        super(CourseModel, self).save(**kwargs)

    def __str__(self) -> str:
        return str(self.course)

    def get_off_price(self):
        price = self.price
        percent_discount = self.percent_discount
        if self.percent_discount is None:
            percent_discount = 0
        return int(price - price * percent_discount / 100)


class SampleExerciseModel(models.Model):

    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_sample')
    category = models.ForeignKey(CourseCategoryModel, on_delete=models.CASCADE, related_name='category_sample')
    subcategory = models.ForeignKey(CourseSubCategoryModel, on_delete=models.CASCADE, related_name='subcategory_sample')
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name='course_sample')
    sample_exercise = models.FileField(upload_to='video/sample/')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category


class OrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_order')
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name='course_order')
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {str(self.id)}'

    def get_total_price(self):
        total = sum(item.get_cost() for item in self.items_order.all())

        return total


class OrderItemModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='items_order')
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name='items_course')
    price = models.IntegerField()

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price
