# Generated by Django 4.2.7 on 2024-02-28 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_ordermodel_authority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='authority',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
