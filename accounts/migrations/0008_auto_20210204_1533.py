# Generated by Django 3.1.5 on 2021-02-04 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210203_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('male', 'female'), ('unknown', 'unknown')], default=3, max_length=10, verbose_name='gender'),
        ),
    ]
