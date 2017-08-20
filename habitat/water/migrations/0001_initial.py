# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 00:19
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('building', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrinkingWater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('date', models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date')),
                ('time', models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time')),
                ('volume', models.DecimalField(decimal_places=2, default=None, help_text='liters', max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9.99)], verbose_name='Volume')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Astronaut')),
            ],
            options={
                'verbose_name': 'Drinking Water Usage',
                'verbose_name_plural': 'Drinking Water',
            },
        ),
        migrations.CreateModel(
            name='GreenWater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('date', models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date')),
                ('time', models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time')),
                ('volume', models.DecimalField(decimal_places=2, default=None, help_text='liters', max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9.99)], verbose_name='Volume')),
                ('usage_description', models.TextField(blank=True, default=None, null=True, verbose_name='Usage Description')),
                ('location', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='building.Module', verbose_name='Usage Location')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Astronaut')),
            ],
            options={
                'verbose_name': 'Green Water Usage',
                'verbose_name_plural': 'Green Water',
            },
        ),
        migrations.CreateModel(
            name='TechnicalWater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('date', models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date')),
                ('time', models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time')),
                ('volume', models.DecimalField(decimal_places=2, default=None, help_text='liters', max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9.99)], verbose_name='Volume')),
                ('usage_description', models.TextField(blank=True, default=None, null=True, verbose_name='Usage Description')),
                ('location', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='building.Module', verbose_name='Usage Location')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Astronaut')),
            ],
            options={
                'verbose_name': 'Technical Water Usage',
                'verbose_name_plural': 'Technical Water',
            },
        ),
    ]
