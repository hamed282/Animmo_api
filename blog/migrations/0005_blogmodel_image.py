# Generated by Django 4.2.7 on 2024-02-10 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogmodel_class_des'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(default=1, upload_to='images/blog/'),
            preserve_default=False,
        ),
    ]
