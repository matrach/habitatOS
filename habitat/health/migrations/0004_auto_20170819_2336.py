# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 23:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_auto_20170819_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodpressure',
            name='date',
            field=models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='bloodpressure',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
        migrations.AlterField(
            model_name='disease',
            name='date',
            field=models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='disease',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
        migrations.AlterField(
            model_name='pulseoxymetry',
            name='date',
            field=models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='pulseoxymetry',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
        migrations.AlterField(
            model_name='stool',
            name='date',
            field=models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='stool',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='date',
            field=models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
        migrations.AlterField(
            model_name='urine',
            name='date',
            field=models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='urine',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='date',
            field=models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
    ]
