# Generated by Django 5.0.3 on 2024-04-07 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0003_remove_usercoursemodel_ref_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercoursemodel',
            name='spotplayer_license',
            field=models.CharField(max_length=512),
        ),
    ]