# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenhouse', '0005_auto_20170520_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='wikipedia_url',
            field=models.URLField(blank=True, default=None, null=True, verbose_name='Wikipedia URL'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='cultivation_method',
            field=models.CharField(choices=[('soil', 'Soil'), ('underwater', 'Underwater'), ('artificial', 'Artificial'), ('hydroponics', 'Hydroponics'), ('aeroponics', 'Aeroponics'), ('mixed', 'Mixed'), ('other', 'Other')], default=None, max_length=30, verbose_name='Cultivation method'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='notes',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name='Image'),
        ),
    ]