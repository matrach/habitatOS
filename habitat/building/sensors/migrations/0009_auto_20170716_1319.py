# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 13:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0008_auto_20170716_1316'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carbondioxide',
            options={'ordering': ['-datetime'], 'verbose_name': 'Carbon Dioxide Concentration Measurement', 'verbose_name_plural': 'Carbon Dioxide'},
        ),
        migrations.AlterModelOptions(
            name='carbonmonoxide',
            options={'ordering': ['-datetime'], 'verbose_name': 'Carbon Monoxide Concentration Measurement', 'verbose_name_plural': 'Carbon Monoxide'},
        ),
        migrations.AlterModelOptions(
            name='oxygen',
            options={'ordering': ['-datetime'], 'verbose_name': 'Oxygen Concentration Measurement', 'verbose_name_plural': 'Oxygen'},
        ),
    ]