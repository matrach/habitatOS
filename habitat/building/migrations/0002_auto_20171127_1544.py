# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='module',
            name='modified',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='modified',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime [UTC]'),
        ),
    ]
