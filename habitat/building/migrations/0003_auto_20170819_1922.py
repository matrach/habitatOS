# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0002_auto_20170819_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='date',
            field=models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='date',
            field=models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Date'),
        ),
    ]
