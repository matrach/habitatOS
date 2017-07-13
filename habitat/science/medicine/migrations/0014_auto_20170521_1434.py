# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 14:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0013_auto_20170521_1326'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloodpressure',
            options={'ordering': ['-datetime'], 'verbose_name': 'Blood Pressure Measurement', 'verbose_name_plural': 'Blood Pressure Database'},
        ),
        migrations.AlterModelOptions(
            name='disease',
            options={'ordering': ['-datetime_start'], 'verbose_name': 'Disease Log', 'verbose_name_plural': 'Disease Logbook'},
        ),
        migrations.AlterModelOptions(
            name='meal',
            options={'ordering': ['-datetime'], 'verbose_name': 'Food Intake', 'verbose_name_plural': 'Food Logbook'},
        ),
        migrations.AlterModelOptions(
            name='pulsoxymetry',
            options={'ordering': ['-datetime'], 'verbose_name': 'Pulse Oxymetry Measurement', 'verbose_name_plural': 'Pulse Oxymetry Database'},
        ),
        migrations.AlterModelOptions(
            name='qualityoflife',
            options={'ordering': ['-datetime'], 'verbose_name': 'Quality of Life Entry', 'verbose_name_plural': 'Quality of Life Entries'},
        ),
        migrations.AlterModelOptions(
            name='sleep',
            options={'ordering': ['-datetime_start'], 'verbose_name': 'Sleep Log', 'verbose_name_plural': 'Sleep Logbook'},
        ),
        migrations.AlterModelOptions(
            name='temperature',
            options={'ordering': ['-datetime'], 'verbose_name': 'Temperature Measurement', 'verbose_name_plural': 'Temperature Database'},
        ),
        migrations.AlterModelOptions(
            name='weight',
            options={'ordering': ['-datetime'], 'verbose_name': 'Weight Measurement', 'verbose_name_plural': 'Weight Database'},
        ),
    ]