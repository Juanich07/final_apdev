# Generated by Django 5.0 on 2023-12-29 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_continent_governmentform_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='flag',
            field=models.ImageField(blank=True, null=True, upload_to='country_flags/'),
        ),
    ]
