# Generated by Django 5.0 on 2023-12-29 08:22

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('country_code', models.CharField(max_length=3)),
                ('district', models.CharField(max_length=100)),
                ('population', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=3, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('continent', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('surface_area', models.FloatField()),
                ('indep_year', models.IntegerField(blank=True, null=True)),
                ('population', models.IntegerField()),
                ('life_expectancy', models.FloatField(blank=True, null=True)),
                ('gnp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('gnp_old', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('local_name', models.CharField(max_length=100)),
                ('government_form', models.CharField(max_length=100)),
                ('head_of_state', models.CharField(max_length=100)),
                ('code2', models.CharField(max_length=2)),
                ('capital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.city')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CountryLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('language', models.CharField(max_length=50)),
                ('is_official', models.BooleanField()),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('country_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.country')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]