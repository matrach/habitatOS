# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0003_auto_20170521_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaryentry',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('scheduled', 'Scheduled')], default='draft', max_length=30, verbose_name='Status'),
        ),
    ]