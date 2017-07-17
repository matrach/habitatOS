# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0008_auto_20170717_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mood',
            name='day_quality',
            field=models.CharField(choices=[('very-good', 'Very Good'), ('good', 'Good'), ('average', 'Average'), ('bad', 'Bad'), ('very-bad', 'Very Bad')], default=None, max_length=30, verbose_name='Day Quality'),
        ),
        migrations.AlterField(
            model_name='mood',
            name='mood',
            field=models.CharField(choices=[('very-high', 'Very High'), ('high', 'High'), ('normal', 'Normal'), ('low', 'Low'), ('very-low', 'Very Low')], default=None, max_length=30, verbose_name='Mood'),
        ),
        migrations.AlterField(
            model_name='mood',
            name='productivity',
            field=models.CharField(choices=[('very-high', 'Very High'), ('high', 'High'), ('normal', 'Normal'), ('low', 'Low'), ('very-low', 'Very Low')], default=None, max_length=30, verbose_name='Productivity'),
        ),
        migrations.AlterField(
            model_name='mood',
            name='stress',
            field=models.CharField(choices=[('very-high', 'Very High'), ('high', 'High'), ('normal', 'Normal'), ('low', 'Low'), ('very-low', 'Very Low')], default=None, max_length=30, verbose_name='Stress'),
        ),
    ]