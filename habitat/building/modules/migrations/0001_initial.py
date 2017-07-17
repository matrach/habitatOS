# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default=None, max_length=255, verbose_name='Name')),
                ('status', models.CharField(choices=[('nominal', 'Working Nominal'), ('locked', 'Locked'), ('disabled', 'Disabled'), ('under-construction', 'Under Construction'), ('destructed', 'Destructed')], db_index=True, default='nominal', max_length=30, verbose_name='Status')),
                ('hazzard', models.CharField(choices=[('none', 'Working Nominal'), ('warning', 'Warning'), ('hazardous', 'Hazardous'), ('toxic', 'Toxic'), ('depress', 'Hazardous'), ('fire', 'Fire'), ('disabled', 'Disabled')], db_index=True, default=None, max_length=30, verbose_name='Status')),
                ('width', models.PositiveIntegerField(blank=True, default=None, help_text='m', null=True, verbose_name='Volume')),
                ('height', models.PositiveIntegerField(blank=True, default=None, help_text='m', null=True, verbose_name='Height')),
                ('length', models.PositiveIntegerField(blank=True, default=None, help_text='m', null=True, verbose_name='Length')),
                ('plan', models.CharField(choices=[('ellipsis', 'Ellipsis'), ('rectangle', 'Rectangle'), ('polygon', 'Polygon'), ('other', 'Other')], default=None, max_length=30, verbose_name='Plan')),
                ('capacity', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Capacity')),
            ],
            options={
                'verbose_name': 'Module',
                'verbose_name_plural': 'Modules',
                'ordering': ['name'],
            },
        ),
    ]
