# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 00:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('extravehicular', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spacewalker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('designation', models.CharField(choices=[('leader', 'Lead Spacewalker'), ('support', 'Supporting Spacewalker')], max_length=30, verbose_name='Designation')),
            ],
            options={
                'verbose_name': 'Spacewalker',
                'verbose_name_plural': 'Spacewalkers',
            },
        ),
        migrations.RemoveField(
            model_name='activity',
            name='participants',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='time',
        ),
        migrations.RemoveField(
            model_name='location',
            name='height',
        ),
        migrations.AddField(
            model_name='activity',
            name='tools',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Tools'),
        ),
        migrations.AddField(
            model_name='location',
            name='direction',
            field=models.CharField(choices=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West'), ('north-east', 'North East'), ('north-east', 'North West'), ('south-east', 'South East'), ('south-east', 'South West')], default='north', max_length=30, verbose_name='Direction from Habitat'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='elevation',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, help_text='Meters AGSL', max_digits=6, null=True, verbose_name='Elevation'),
        ),
        migrations.RemoveField(
            model_name='activity',
            name='contingencies',
        ),
        migrations.AddField(
            model_name='activity',
            name='contingencies',
            field=models.ManyToManyField(to='extravehicular.Contingency', verbose_name='Contingencies'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='end',
            field=models.TimeField(blank=True, default=None, null=True, verbose_name='End'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='objectives',
            field=models.TextField(verbose_name='Objectives'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start',
            field=models.TimeField(blank=True, null=True, verbose_name='Start'),
        ),
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.TextField(blank=True, default=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=7, default=None, help_text='Decimal Degrees', max_digits=10, null=True, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=7, default=None, help_text='Decimal Degrees', max_digits=9, null=True, verbose_name='Longitude'),
        ),
        migrations.AlterField(
            model_name='report',
            name='time',
            field=models.TimeField(help_text='Lunar Standard Time', verbose_name='Mission Time', default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='spacewalker',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extravehicular.Activity', verbose_name='Activity'),
        ),
        migrations.AddField(
            model_name='spacewalker',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Participant'),
        ),
    ]
