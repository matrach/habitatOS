# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 20:46
from __future__ import unicode_literals

from django.db import migrations, models
import habitat.timezone.models.martian_standard_time


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodpressure',
            name='date',
            field=models.CharField(default=habitat.timezone.models.martian_standard_time.MartianStandardTime.date, help_text='example: 51099.420109, <a href="/api/v1/timezone/martian-standard-time/converter/" target="_blank">use converter</a> to calculate from Earth time', max_length=15, verbose_name='Mars Sol Date'),
        ),
        migrations.AlterField(
            model_name='bloodpressure',
            name='time',
            field=models.TimeField(default=habitat.timezone.models.martian_standard_time.MartianStandardTime.time, help_text='example: 16:04:57, <a href="/api/v1/timezone/martian-standard-time/converter/" target="_blank">use converter</a> to calculate from Earth time', verbose_name='Coordinated Mars Time'),
        ),
        migrations.AlterField(
            model_name='disease',
            name='date',
            field=models.CharField(default=habitat.timezone.models.martian_standard_time.MartianStandardTime.date, help_text='example: 51099.420109, <a href="/api/v1/timezone/martian-standard-time/converter/" target="_blank">use converter</a> to calculate from Earth time', max_length=15, verbose_name='Mars Sol Date'),
        ),
        migrations.AlterField(
            model_name='disease',
            name='time',
            field=models.TimeField(default=habitat.timezone.models.martian_standard_time.MartianStandardTime.time, help_text='example: 16:04:57, <a href="/api/v1/timezone/martian-standard-time/converter/" target="_blank">use converter</a> to calculate from Earth time', verbose_name='Coordinated Mars Time'),
        ),
        migrations.AlterField(
            model_name='pulseoxymetry',
            name='date',
            field=models.CharField(default=habitat.timezone.models.martian_standard_time.MartianStandardTime.date, help_text='example: 51099.420109, <a href="/api/v1/timezone/martian-standard-time/converter/" target="_blank">use converter</a> to calculate from Earth time', max_length=15, verbose_name='Mars Sol Date'),
        ),
        migrations.AlterField(
            model_name='pulseoxymetry',
            name='time',
            field=models.TimeField(default=habitat.timezone.models.martian_standard_time.MartianStandardTime.time, help_text='example: 16:04:57, <a href="/api/v1/timezone/martian-standard-time/converter/" target="_blank">use converter</a> to calculate from Earth time', verbose_name='Coordinated Mars Time'),
        ),
        migrations.AlterField(
            model_name='stool',
            name='date',
            field=models.CharField(default=habitat.timezone.models.martian_standard_time.MartianStandardTime.date, help_text='example: 51099.420109, <a href="/api/v1/timezone/martian-standard-time/converter/" target="_blank">use converter</a> to calculate from Earth time', max_length=15, verbose_name='Mars Sol Date'),
        ),
        migrations.AlterField(
            model_name='stool',
            name='time',
            field=models.TimeField(default=habitat.timezone.models.martian_standard_time.MartianStandardTime.time, help_text='example: 16:04:57, <a href="/api/v1/timezone/martian-standard-time/converter/" target="_blank">use converter</a> to calculate from Earth time', verbose_name='Coordinated Mars Time'),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='date',
            field=models.CharField(default=habitat.timezone.models.martian_standard_time.MartianStandardTime.date, help_text='example: 51099.420109, <a href="/api/v1/timezone/martian-standard-time/converter/" target="_blank">use converter</a> to calculate from Earth time', max_length=15, verbose_name='Mars Sol Date'),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='time',
            field=models.TimeField(default=habitat.timezone.models.martian_standard_time.MartianStandardTime.time, help_text='example: 16:04:57, <a href="/api/v1/timezone/martian-standard-time/converter/" target="_blank">use converter</a> to calculate from Earth time', verbose_name='Coordinated Mars Time'),
        ),
        migrations.AlterField(
            model_name='urine',
            name='date',
            field=models.CharField(default=habitat.timezone.models.martian_standard_time.MartianStandardTime.date, help_text='example: 51099.420109, <a href="/api/v1/timezone/martian-standard-time/converter/" target="_blank">use converter</a> to calculate from Earth time', max_length=15, verbose_name='Mars Sol Date'),
        ),
        migrations.AlterField(
            model_name='urine',
            name='time',
            field=models.TimeField(default=habitat.timezone.models.martian_standard_time.MartianStandardTime.time, help_text='example: 16:04:57, <a href="/api/v1/timezone/martian-standard-time/converter/" target="_blank">use converter</a> to calculate from Earth time', verbose_name='Coordinated Mars Time'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='date',
            field=models.CharField(default=habitat.timezone.models.martian_standard_time.MartianStandardTime.date, help_text='example: 51099.420109, <a href="/api/v1/timezone/martian-standard-time/converter/" target="_blank">use converter</a> to calculate from Earth time', max_length=15, verbose_name='Mars Sol Date'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='time',
            field=models.TimeField(default=habitat.timezone.models.martian_standard_time.MartianStandardTime.time, help_text='example: 16:04:57, <a href="/api/v1/timezone/martian-standard-time/converter/" target="_blank">use converter</a> to calculate from Earth time', verbose_name='Coordinated Mars Time'),
        ),
    ]