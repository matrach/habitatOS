# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 00:19
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('building', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarbonDioxide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('date', models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date')),
                ('time', models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time')),
                ('value', models.DecimalField(decimal_places=3, help_text='%', max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Concentration')),
                ('location', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='building.Module', verbose_name='Sensor Location')),
            ],
            options={
                'verbose_name': 'Carbon Dioxide Concentration Measurement',
                'verbose_name_plural': 'Carbon Dioxide',
            },
        ),
        migrations.CreateModel(
            name='CarbonMonoxide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('date', models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date')),
                ('time', models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time')),
                ('value', models.DecimalField(decimal_places=3, help_text='%', max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Concentration')),
                ('location', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='building.Module', verbose_name='Sensor Location')),
            ],
            options={
                'verbose_name': 'Carbon Monoxide Concentration Measurement',
                'verbose_name_plural': 'Carbon Monoxide',
            },
        ),
        migrations.CreateModel(
            name='Humidity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('date', models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date')),
                ('time', models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time')),
                ('value', models.DecimalField(decimal_places=1, help_text='%', max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Humidity')),
                ('location', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='building.Module', verbose_name='Sensor Location')),
            ],
            options={
                'verbose_name': 'Humidity Measurement',
                'verbose_name_plural': 'Humidity',
            },
        ),
        migrations.CreateModel(
            name='Luminance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('date', models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date')),
                ('time', models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time')),
                ('value', models.PositiveSmallIntegerField(default=None, help_text='lumen', verbose_name='Luminance')),
                ('location', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='building.Module', verbose_name='Sensor Location')),
            ],
            options={
                'verbose_name': 'Luminance Measurement',
                'verbose_name_plural': 'Luminance',
            },
        ),
        migrations.CreateModel(
            name='Meteo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('date', models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date')),
                ('time', models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time')),
                ('value', models.PositiveSmallIntegerField(default=None, verbose_name='Value')),
                ('location', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='building.Module', verbose_name='Sensor Location')),
            ],
            options={
                'verbose_name': 'Meteo',
                'verbose_name_plural': 'Meteo Measurements',
            },
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('date', models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date')),
                ('time', models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time')),
                ('value', models.DecimalField(decimal_places=2, default=None, help_text='Mbps', max_digits=5, verbose_name='Value')),
                ('location', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='building.Module', verbose_name='Sensor Location')),
            ],
            options={
                'verbose_name': 'Network Performance Measurement',
                'verbose_name_plural': 'Network Performance',
            },
        ),
        migrations.CreateModel(
            name='Oxygen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('date', models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date')),
                ('time', models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time')),
                ('value', models.DecimalField(decimal_places=2, help_text='%', max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Concentration')),
                ('location', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='building.Module', verbose_name='Sensor Location')),
            ],
            options={
                'verbose_name': 'Oxygen Concentration Measurement',
                'verbose_name_plural': 'Oxygen',
            },
        ),
        migrations.CreateModel(
            name='Pressure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('date', models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date')),
                ('time', models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time')),
                ('value', models.DecimalField(decimal_places=2, default=None, help_text='mmHg', max_digits=6, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2000)], verbose_name='Pressure')),
                ('location', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='building.Module', verbose_name='Sensor Location')),
            ],
            options={
                'verbose_name': 'Pressure Measurement',
                'verbose_name_plural': 'Pressure',
            },
        ),
        migrations.CreateModel(
            name='Radiation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('date', models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date')),
                ('time', models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time')),
                ('value', models.DecimalField(decimal_places=5, default=None, help_text='Sievert', max_digits=6, verbose_name='Radiation')),
                ('location', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='building.Module', verbose_name='Sensor Location')),
            ],
            options={
                'verbose_name': 'Radiation Measurement',
                'verbose_name_plural': 'Radiation',
            },
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('date', models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date')),
                ('time', models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time')),
                ('value', models.DecimalField(decimal_places=2, default=None, max_digits=5, verbose_name='Temperature')),
                ('unit', models.CharField(choices=[('celsius', 'Celsius'), ('kelvin', 'Kelvin'), ('fahrenheit', 'Fahrenheit')], default='celsius', max_length=10, verbose_name='Unit')),
                ('location', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='building.Module', verbose_name='Sensor Location')),
            ],
            options={
                'verbose_name': 'Temperature Measurement',
                'verbose_name_plural': 'Temperature',
            },
        ),
        migrations.CreateModel(
            name='Voltage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('date', models.CharField(default=None, help_text='Lunar Standard Time', max_length=15, verbose_name='Mission Date')),
                ('time', models.TimeField(default=django.utils.timezone.now, help_text='Lunar Standard Time', verbose_name='Mission Time')),
                ('value', models.DecimalField(decimal_places=3, default=None, help_text='Volts', max_digits=6, verbose_name='Value')),
                ('location', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='building.Module', verbose_name='Sensor Location')),
            ],
            options={
                'verbose_name': 'Voltage Measurement',
                'verbose_name_plural': 'Voltage',
            },
        ),
    ]
