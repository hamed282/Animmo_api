# Generated by Django 4.2.7 on 2024-02-28 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_ordermodel_authority'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='ref_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
