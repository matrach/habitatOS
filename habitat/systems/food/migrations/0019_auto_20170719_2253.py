# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0018_auto_20170719_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayplan',
            name='diet',
            field=models.ManyToManyField(blank=True, default=None, to='food.Diet', verbose_name='Diet'),
        ),
    ]
