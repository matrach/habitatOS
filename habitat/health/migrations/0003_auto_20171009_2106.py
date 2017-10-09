# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 21:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0002_auto_20171009_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urine',
            name='volume',
            field=models.PositiveIntegerField(default=None, help_text='ml', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5000)], verbose_name='Volume'),
        ),
    ]
