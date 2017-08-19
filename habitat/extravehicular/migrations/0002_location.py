# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 22:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('extravehicular', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('date', models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Date')),
                ('time', models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Time')),
                ('identifier', models.CharField(max_length=10, unique=True, verbose_name='Identifier')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, default=None, help_text='Decimal Degrees', max_digits=9, null=True, verbose_name='Longitude')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, default=None, help_text='Decimal Degrees', max_digits=9, null=True, verbose_name='Latitude')),
                ('height', models.DecimalField(blank=True, decimal_places=2, default=None, help_text='Meters', max_digits=6, null=True, verbose_name='Height')),
                ('radius', models.DecimalField(blank=True, decimal_places=2, default=None, help_text='Meters', max_digits=6, null=True, verbose_name='Radius')),
            ],
            options={
                'verbose_name': 'Contingency',
                'verbose_name_plural': 'Contingencies',
            },
        ),
    ]
