# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_auto_20170713_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(default=None, to='food.Tag', verbose_name='Tags'),
        ),
    ]
