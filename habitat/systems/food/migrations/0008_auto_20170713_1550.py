# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_auto_20170713_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, default=None, to='food.Tag', verbose_name='Tags'),
        ),
    ]
