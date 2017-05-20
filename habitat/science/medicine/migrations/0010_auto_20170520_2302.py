# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 23:02
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0009_auto_20170520_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='body_fat',
            field=models.DecimalField(decimal_places=1, default=None, help_text='%', max_digits=3, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='Body Fat', null=True, blank=True),
        ),
    ]
