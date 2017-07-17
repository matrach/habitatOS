# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 12:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spicies', models.CharField(help_text='Latin', max_length=255, verbose_name='Species')),
            ],
        ),
        migrations.AddField(
            model_name='experiment',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biolab.Plant', verbose_name='Plant'),
        ),
    ]