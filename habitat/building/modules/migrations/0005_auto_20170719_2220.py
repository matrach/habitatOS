# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0004_auto_20170717_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='hazzard',
            field=models.CharField(choices=[('none', 'None'), ('warning', 'Warning'), ('hazardous', 'Hazardous'), ('toxic', 'Toxic'), ('depress', 'Hazardous'), ('fire', 'Fire'), ('disabled', 'Disabled')], db_index=True, default=None, max_length=30, verbose_name='Hazzard'),
        ),
    ]