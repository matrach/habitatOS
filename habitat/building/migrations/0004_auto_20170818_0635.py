# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 06:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0003_storage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storage',
            options={'ordering': ['name'], 'verbose_name': 'Storage', 'verbose_name_plural': 'Storage'},
        ),
    ]
