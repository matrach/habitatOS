# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 17:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0004_auto_20170825_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='location',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='building.Module', verbose_name='Location'),
        ),
    ]
