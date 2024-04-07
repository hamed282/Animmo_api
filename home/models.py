from django.db import models
from accounts.models import User
from django.utils.html import mark_safe
from django_ckeditor_5.fields import CKEditor5Field


class HomeSettingModel(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    banner = models.ImageField(upload_to='images/header')
    header_logo = models.FileField(upload_to='images/home_setting/')
    footer_logo = models.FileField(upload_to='images/home_setting/')
    class_des = models.CharField(max_length=20, default='image_header')

    def banner_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.banner.url))
    banner_tag.short_description = 'Image'


class FeedbackModel(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rel_user_feedback')
    message = models.TextField(max_length=160)
    available = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    class_des = models.CharField(max_length=20, default='feedback')


class GuideModel(models.Model):
    objects = None
    faq = CKEditor5Field(config_name='extends')
    spot_player = CKEditor5Field(config_name='extends')


class HitsCountModel(models.Model):
    objects = None
    ip = models.CharField(max_length=64)
    mac = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)


class TotalHitsModel(models.Model):
    objects = None
    hits = models.IntegerField(default=0)
    date = models.DateField()
