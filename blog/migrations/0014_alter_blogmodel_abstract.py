# Generated by Django 5.0.3 on 2024-04-21 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_blogmodel_abstract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='abstract',
            field=models.CharField(max_length=200),
        ),
    ]
