# Generated by Django 5.0.3 on 2024-04-07 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_spot_guidemodel_spot_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='HitsCountModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=64)),
                ('mac', models.CharField(max_length=64)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TotalHitsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hits', models.IntegerField(default=0)),
                ('date', models.DateField()),
            ],
        ),
    ]
