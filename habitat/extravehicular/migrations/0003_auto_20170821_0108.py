# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 01:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extravehicular', '0002_auto_20170821_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='contingencies',
            field=models.ManyToManyField(blank=True, default=None, to='extravehicular.Contingency', verbose_name='Contingencies'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='location',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='extravehicular.Location', verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Description'),
        ),
    ]
