# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 18:53
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('name', models.CharField(db_index=True, default=None, max_length=255, verbose_name='Name')),
                ('status', models.CharField(choices=[('nominal', 'Working Nominal'), ('locked', 'Locked'), ('disabled', 'Disabled'), ('under-construction', 'Under Construction'), ('destructed', 'Destructed')], db_index=True, default='nominal', max_length=30, verbose_name='Status')),
                ('hazard', models.CharField(choices=[('none', 'None'), ('warning', 'Warning'), ('hazardous', 'Hazardous'), ('toxic', 'Toxic'), ('depress', 'Hazardous'), ('fire', 'Fire'), ('disabled', 'Disabled')], db_index=True, default='none', max_length=30, verbose_name='Hazard')),
                ('blueprint', models.ImageField(blank=True, default=None, null=True, upload_to='building/', verbose_name='Blueprint')),
                ('width', models.DecimalField(blank=True, decimal_places=2, default=None, help_text='m', max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)], verbose_name='Width')),
                ('height', models.DecimalField(blank=True, decimal_places=2, default=None, help_text='m', max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)], verbose_name='Height')),
                ('length', models.DecimalField(blank=True, decimal_places=2, default=None, help_text='m', max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)], verbose_name='Length')),
                ('plan', models.CharField(choices=[('ellipsis', 'Ellipsis'), ('rectangle', 'Rectangle'), ('polygon', 'Polygon'), ('other', 'Other')], default='rectangle', max_length=30, verbose_name='Plan')),
                ('capacity', models.PositiveIntegerField(blank=True, default=None, help_text='Max crew members working inside.', null=True, verbose_name='Capacity')),
            ],
            options={
                'verbose_name': 'Module',
                'verbose_name_plural': 'Modules',
            },
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='building.Module', verbose_name='location')),
            ],
            options={
                'verbose_name': 'Storage',
                'verbose_name_plural': 'Storage',
            },
        ),
    ]
