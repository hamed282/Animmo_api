# Generated by Django 5.0.3 on 2024-04-21 14:14

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_blogmodel_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]
