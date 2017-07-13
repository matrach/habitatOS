# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 13:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0012_auto_20170521_1259'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloodpressure',
            options={'ordering': ['-datetime'], 'verbose_name': 'Blood Pressure Database'},
        ),
        migrations.AlterModelOptions(
            name='disease',
            options={'ordering': ['-datetime_start'], 'verbose_name': 'Disease Logbook'},
        ),
        migrations.AlterModelOptions(
            name='meal',
            options={'ordering': ['-datetime'], 'verbose_name': 'Food Logbook'},
        ),
        migrations.AlterModelOptions(
            name='pulsoxymetry',
            options={'ordering': ['-datetime'], 'verbose_name': 'Pulse Oxymetry Database'},
        ),
        migrations.AlterModelOptions(
            name='qualityoflife',
            options={'ordering': ['-datetime'], 'verbose_name': 'Quality of Life Entries'},
        ),
        migrations.AlterModelOptions(
            name='sleep',
            options={'ordering': ['-datetime_start'], 'verbose_name': 'Sleep Logbook'},
        ),
        migrations.AlterModelOptions(
            name='temperature',
            options={'ordering': ['-datetime'], 'verbose_name': 'Temperature Database'},
        ),
        migrations.AlterModelOptions(
            name='weight',
            options={'ordering': ['-datetime'], 'verbose_name': 'Weight Database'},
        ),
    ]