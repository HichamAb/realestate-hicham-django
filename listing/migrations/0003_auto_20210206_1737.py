# Generated by Django 3.1.5 on 2021-02-06 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_auto_20210206_1735'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name': 'State', 'verbose_name_plural': 'States'},
        ),
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.city', verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.state', verbose_name='state'),
        ),
    ]
