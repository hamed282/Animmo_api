from django.db import models
from accounts.models import User
from django_ckeditor_5.fields import CKEditor5Field
from tinymce.models import HTMLField
from django.utils.text import slugify


class BlogModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rel_user_blog')
    banner = models.ImageField(upload_to='images/blog/banner/')
    title = models.CharField(max_length=50)
    # body = CKEditor5Field(config_name='extends')
    body = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='images/blog/images/')
    available = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)

    def save(self, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(BlogModel, self).save(**kwargs)

    def __str__(self):
        return f'{self.title}'
