# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0010_auto_20170926_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zwavesensor',
            name='type',
            field=models.CharField(choices=[('battery-level', 'Battery Level'), ('powerlevel', 'Power Level'), ('temperature', 'Temperature'), ('luminance', 'Luminance'), ('relative-humidity', 'Relative Humidity'), ('ultraviolet', 'Ultraviolet'), ('burglar', 'Burglar')], max_length=30, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='zwavesensor',
            name='unit',
            field=models.CharField(blank=True, choices=[('percent', '%'), ('lux', 'Lux'), ('decibel', 'dB'), ('celsius', 'Celsius'), ('kelvin', 'Kelvin'), ('fahrenheit', 'Fahrenheit')], default=None, max_length=15, null=True, verbose_name='Unit'),
        ),
    ]
