# Generated by Django 3.1.5 on 2021-02-04 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20210204_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username_id',
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='username'),
        ),
    ]
