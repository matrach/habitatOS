# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0002_auto_20171009_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carbondioxide',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='carbondioxide',
            name='modified',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='carbonmonoxide',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='carbonmonoxide',
            name='modified',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='humidity',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='humidity',
            name='modified',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='illuminance',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='illuminance',
            name='modified',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='network',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='network',
            name='modified',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='oxygen',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='oxygen',
            name='modified',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='pressure',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='pressure',
            name='modified',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='radiation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='radiation',
            name='modified',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='modified',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='voltage',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='voltage',
            name='modified',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='modified',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='zwavesensor',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='zwavesensor',
            name='datetime',
            field=models.DateTimeField(db_index=True, editable=False, verbose_name='Datetime [UTC]'),
        ),
        migrations.AlterField(
            model_name='zwavesensor',
            name='device',
            field=models.CharField(choices=[('c1344062-2', 'Atrium'), ('c1344062-3', 'Analytic Lab'), ('c1344062-4', 'Operations'), ('c1344062-5', 'Toilet'), ('c1344062-6', 'Dormitory'), ('c1344062-7', 'Storage'), ('c1344062-8', 'Kitchen'), ('c1344062-9', 'Biolab')], db_index=True, max_length=30, verbose_name='Device'),
        ),
        migrations.AlterField(
            model_name='zwavesensor',
            name='modified',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime [UTC]'),
        ),
    ]
