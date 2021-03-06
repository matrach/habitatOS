# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 18:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import habitat.timezone.models.martian_standard_time


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('date', models.CharField(default=habitat.timezone.models.martian_standard_time.MartianStandardTime.date, help_text='example: 51099.420109', max_length=15, verbose_name='Mars Sol Date')),
                ('start', models.TimeField(blank=True, default=None, null=True, verbose_name='EVA Start')),
                ('end', models.TimeField(blank=True, default=None, null=True, verbose_name='EVA End')),
                ('objectives', models.TextField(verbose_name='Objectives')),
            ],
            options={
                'verbose_name': 'Extra-Vehicular Activity',
                'verbose_name_plural': 'Extra-Vehicular Activities',
            },
        ),
        migrations.CreateModel(
            name='Contingency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('identifier', models.CharField(max_length=10, unique=True, verbose_name='Identifier')),
                ('severity', models.CharField(choices=[('emergency', 'Emergency - ABORT the simulation'), ('critical', 'Critical - ABORT the EVA'), ('warning', 'Warning'), ('info', 'Informative')], default='info', max_length=30, verbose_name='Severity')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('recovery_procedure', models.TextField(verbose_name='Recovery Procedure')),
                ('remarks', models.TextField(blank=True, default=None, null=True, verbose_name='Additional Remarks')),
            ],
            options={
                'verbose_name': 'Contingency',
                'verbose_name_plural': 'Contingencies',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('identifier', models.CharField(max_length=10, unique=True, verbose_name='Identifier')),
                ('direction', models.CharField(choices=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West'), ('north-east', 'North East'), ('north-east', 'North West'), ('south-east', 'South East'), ('south-east', 'South West')], max_length=30, verbose_name='Direction from Habitat')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, default=None, null=True, verbose_name='Description')),
                ('longitude', models.DecimalField(blank=True, decimal_places=7, default=None, help_text='Decimal Degrees', max_digits=9, null=True, verbose_name='Longitude')),
                ('latitude', models.DecimalField(blank=True, decimal_places=7, default=None, help_text='Decimal Degrees', max_digits=10, null=True, verbose_name='Latitude')),
                ('elevation', models.DecimalField(blank=True, decimal_places=2, default=None, help_text='Meters AGSL', max_digits=6, null=True, verbose_name='Elevation')),
                ('radius', models.DecimalField(blank=True, decimal_places=2, default=None, help_text='Meters', max_digits=6, null=True, verbose_name='Radius')),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('identifier', models.CharField(max_length=10, unique=True, verbose_name='Identifier')),
                ('estimated_duration', models.DurationField(blank=True, default=None, null=True, verbose_name='Estimated Duration')),
                ('objective', models.TextField(verbose_name='Objective')),
                ('remarks', models.TextField(verbose_name='Additional Remarks')),
                ('location', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='extravehicular.Location', verbose_name='Location')),
            ],
            options={
                'verbose_name': 'Objective',
                'verbose_name_plural': 'Objectives',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('date', models.CharField(default=habitat.timezone.models.martian_standard_time.MartianStandardTime.date, help_text='example: 51099.420109', max_length=15, verbose_name='Mars Sol Date')),
                ('time', models.TimeField(default=habitat.timezone.models.martian_standard_time.MartianStandardTime.time, help_text='example: 51099.420109', verbose_name='Coordinated Mars Time')),
                ('start', models.TimeField(blank=True, default=None, null=True, verbose_name='Start')),
                ('end', models.TimeField(blank=True, default=None, null=True, verbose_name='End')),
                ('status', models.CharField(choices=[('success-full', 'Full Success'), ('success-primary', 'Primary Objectives Done'), ('success-partial', 'Partial Success'), ('todo', 'To Do'), ('in-progress', 'In Progress'), ('aborted', 'Aborted')], default='todo', max_length=30, verbose_name='Status')),
                ('type', models.CharField(choices=[('exploratory', 'Exploratory'), ('experimental', 'Experimental'), ('operational', 'Operational'), ('emergency', 'Emergency')], default='operational', max_length=30, verbose_name='Type')),
                ('description', models.TextField(blank=True, default=None, null=True, verbose_name='Description')),
                ('contingencies', models.TextField(blank=True, default=None, null=True, verbose_name='Contingencies')),
                ('remarks', models.TextField(blank=True, default=None, null=True, verbose_name='Contingencies')),
                ('location', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='extravehicular.Location', verbose_name='Location')),
                ('primary_objectives', models.ManyToManyField(related_name='primary_objectives', to='extravehicular.Objective', verbose_name='Primary Objectives')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Astronaut')),
                ('secondary_objectives', models.ManyToManyField(blank=True, default=None, related_name='secondary_objectives', to='extravehicular.Objective', verbose_name='Secondary Objectives')),
            ],
            options={
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
            },
        ),
        migrations.CreateModel(
            name='ReportAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('file', models.FileField(upload_to='report/', verbose_name='Attachment')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extravehicular.Report', verbose_name='Report')),
            ],
            options={
                'verbose_name': 'Report Attachment',
                'verbose_name_plural': 'Report Attachments',
            },
        ),
        migrations.CreateModel(
            name='Spacewalker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Add Datetime')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified Datetime')),
                ('designation', models.CharField(choices=[('ev-leader', 'Lead Spacewalker'), ('ev-support', 'Supporting Spacewalker'), ('habitat-support', 'Habitat Support'), ('rover-operator', 'Rover Operator')], max_length=30, verbose_name='Designation')),
                ('objectives', models.TextField(blank=True, default=None, null=True, verbose_name='Objectives')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extravehicular.Activity', verbose_name='Activity')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Participant')),
            ],
            options={
                'verbose_name': 'Spacewalker',
                'verbose_name_plural': 'Spacewalkers',
            },
        ),
        migrations.AddField(
            model_name='activity',
            name='contingencies',
            field=models.ManyToManyField(blank=True, default=None, to='extravehicular.Contingency', verbose_name='Contingencies'),
        ),
        migrations.AddField(
            model_name='activity',
            name='location',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='extravehicular.Location', verbose_name='Location'),
        ),
        migrations.AddField(
            model_name='activity',
            name='tools',
            field=models.ManyToManyField(blank=True, default=None, to='inventory.Item', verbose_name='Tools'),
        ),
    ]
