# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 23:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0003_auto_20170819_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='date',
        ),
        migrations.RemoveField(
            model_name='module',
            name='time',
        ),
        migrations.RemoveField(
            model_name='storage',
            name='date',
        ),
        migrations.RemoveField(
            model_name='storage',
            name='time',
        ),
    ]
