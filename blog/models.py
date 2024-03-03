from django.db import models
from accounts.models import User
from django_ckeditor_5.fields import CKEditor5Field


class BlogModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rel_user_blog')
    banner = models.ImageField(upload_to='images/blog/banner/')
    title = models.CharField(max_length=50)
    body = CKEditor5Field(config_name='extends')
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='images/blog/images/')
    available = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
