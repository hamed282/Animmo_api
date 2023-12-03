from django.db import models
from accounts.models import User


class HeaderImageModel(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/header')
    class_des = models.CharField(max_length=20, default='image_header')


class FeedbackModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rel_user_feedback')
    message = models.TextField(max_length=160)
    available = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    class_des = models.CharField(max_length=20, default='feedback')

