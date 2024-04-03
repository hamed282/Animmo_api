from django.contrib import admin
from .models import BlogModel


class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]
    list_display = ['user', 'title']


admin.site.register(BlogModel, BlogAdmin)
