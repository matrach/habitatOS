# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 01:45
from __future__ import unicode_literals

from django.db import migrations, models
import habitat._common.models.date


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0004_auto_20170821_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carbondioxide',
            name='date',
            field=models.CharField(default=habitat._common.models.date.lunar_standard_time, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='carbondioxide',
            name='time',
            field=models.TimeField(default=None, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
        migrations.AlterField(
            model_name='carbonmonoxide',
            name='date',
            field=models.CharField(default=habitat._common.models.date.lunar_standard_time, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='carbonmonoxide',
            name='time',
            field=models.TimeField(default=None, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
        migrations.AlterField(
            model_name='humidity',
            name='date',
            field=models.CharField(default=habitat._common.models.date.lunar_standard_time, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='humidity',
            name='time',
            field=models.TimeField(default=None, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
        migrations.AlterField(
            model_name='illuminance',
            name='date',
            field=models.CharField(default=habitat._common.models.date.lunar_standard_time, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='illuminance',
            name='time',
            field=models.TimeField(default=None, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
        migrations.AlterField(
            model_name='network',
            name='date',
            field=models.CharField(default=habitat._common.models.date.lunar_standard_time, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='network',
            name='time',
            field=models.TimeField(default=None, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
        migrations.AlterField(
            model_name='oxygen',
            name='date',
            field=models.CharField(default=habitat._common.models.date.lunar_standard_time, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='oxygen',
            name='time',
            field=models.TimeField(default=None, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
        migrations.AlterField(
            model_name='pressure',
            name='date',
            field=models.CharField(default=habitat._common.models.date.lunar_standard_time, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='pressure',
            name='time',
            field=models.TimeField(default=None, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
        migrations.AlterField(
            model_name='radiation',
            name='date',
            field=models.CharField(default=habitat._common.models.date.lunar_standard_time, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='radiation',
            name='time',
            field=models.TimeField(default=None, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='date',
            field=models.CharField(default=habitat._common.models.date.lunar_standard_time, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='time',
            field=models.TimeField(default=None, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
        migrations.AlterField(
            model_name='voltage',
            name='date',
            field=models.CharField(default=habitat._common.models.date.lunar_standard_time, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='voltage',
            name='time',
            field=models.TimeField(default=None, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='date',
            field=models.CharField(default=habitat._common.models.date.lunar_standard_time, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='time',
            field=models.TimeField(default=None, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
    ]