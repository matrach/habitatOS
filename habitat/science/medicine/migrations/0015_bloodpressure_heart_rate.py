# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-13 08:12
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0014_auto_20170521_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodpressure',
            name='heart_rate',
            field=models.PositiveSmallIntegerField(default=0, help_text='bpm', validators=[django.core.validators.MaxValueValidator(250), django.core.validators.MinValueValidator(0)], verbose_name='Heart Rate'),
            preserve_default=False,
        ),
    ]
