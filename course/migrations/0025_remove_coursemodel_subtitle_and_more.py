# Generated by Django 5.0.3 on 2024-04-17 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0024_coursemodel_subtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursemodel',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='coursemodel',
            name='spot_player_license_subtitle',
            field=models.CharField(default=1, max_length=512),
            preserve_default=False,
        ),
    ]
