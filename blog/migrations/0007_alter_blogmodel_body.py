# Generated by Django 5.0.3 on 2024-03-29 18:00

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_blogmodel_class_des_blogmodel_banner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]
