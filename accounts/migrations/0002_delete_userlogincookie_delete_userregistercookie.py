# Generated by Django 4.2.6 on 2023-10-09 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserLoginCookie',
        ),
        migrations.DeleteModel(
            name='UserRegisterCookie',
        ),
    ]
