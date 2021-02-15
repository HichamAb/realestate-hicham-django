# Generated by Django 3.1.5 on 2021-02-09 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0008_remove_listing_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listingimage',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='listing.listing'),
        ),
    ]
