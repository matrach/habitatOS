# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 23:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0008_waste'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incident',
            old_name='datetime_end',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='incident',
            old_name='datetime_start',
            new_name='start',
        ),
        migrations.RemoveField(
            model_name='mood',
            name='day',
        ),
        migrations.RemoveField(
            model_name='sleep',
            name='time',
        ),
        migrations.AlterField(
            model_name='communication',
            name='date',
            field=models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='date',
            field=models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
        migrations.AlterField(
            model_name='mood',
            name='date',
            field=models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='mood',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
        migrations.AlterField(
            model_name='repair',
            name='date',
            field=models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='repair',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='date',
            field=models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='waste',
            name='date',
            field=models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date'),
        ),
        migrations.AlterField(
            model_name='waste',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
    ]
