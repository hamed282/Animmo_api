# Generated by Django 4.2.7 on 2024-02-21 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0018_remove_coursecategorymodel_class_des_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesubcategorymodel',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coursesubcategorymodel',
            name='subcategory',
            field=models.CharField(max_length=50),
        ),
    ]
