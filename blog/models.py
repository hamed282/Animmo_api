from django.db import models
from accounts.models import User


class BlogModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rel_user_blog')
    title = models.CharField(max_length=50)
    body = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='images/blog/')
    available = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    class_des = models.CharField(max_length=20, default='blog')
