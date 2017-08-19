# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0003_auto_20170819_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinkingwater',
            name='date',
            field=models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='drinkingwater',
            name='time',
            field=models.TimeField(default=None, help_text='Lunar Standard Time', verbose_name='Time'),
        ),
        migrations.AlterField(
            model_name='greenwater',
            name='date',
            field=models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='greenwater',
            name='time',
            field=models.TimeField(default=None, help_text='Lunar Standard Time', verbose_name='Time'),
        ),
    ]
