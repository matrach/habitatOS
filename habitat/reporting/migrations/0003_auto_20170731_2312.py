# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0002_repair'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair',
            name='what',
            field=models.CharField(default=None, max_length=255, verbose_name='What'),
        ),
    ]
