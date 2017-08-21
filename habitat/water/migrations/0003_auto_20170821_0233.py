# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 02:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0002_auto_20170821_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinkingwater',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
        migrations.AlterField(
            model_name='greenwater',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
        migrations.AlterField(
            model_name='technicalwater',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time'),
        ),
    ]
