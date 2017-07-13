# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenhouse', '0006_auto_20170520_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='latin_name',
            field=models.CharField(default=None, max_length=255, verbose_name='Latin Name'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='spicies',
            field=models.CharField(default=None, max_length=255, verbose_name='Species'),
        ),
    ]