# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 12:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0001_initial'),
        ('sensors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Illuminance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('date', models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date')),
                ('time', models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time')),
                ('value', models.PositiveSmallIntegerField(default=None, help_text='Lux', verbose_name='Illuminance')),
                ('location', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='building.Module', verbose_name='Sensor Location')),
            ],
            options={
                'verbose_name': 'Illuminance Measurement',
                'verbose_name_plural': 'Illuminance',
            },
        ),
        migrations.RemoveField(
            model_name='luminance',
            name='location',
        ),
        migrations.DeleteModel(
            name='Luminance',
        ),
    ]