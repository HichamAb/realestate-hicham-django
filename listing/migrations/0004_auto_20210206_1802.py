# Generated by Django 3.1.5 on 2021-02-06 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listing', '0003_auto_20210206_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
