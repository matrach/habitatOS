# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 10:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Datetime')),
                ('stress', models.CharField(blank=True, choices=[('very bad', 'Very Bad'), ('bad', 'Bad'), ('average', 'Average'), ('good', 'Good'), ('very good', 'Very Good')], default=None, max_length=30, null=True, verbose_name='Stress')),
                ('mood', models.CharField(blank=True, choices=[('very bad', 'Very Bad'), ('bad', 'Bad'), ('average', 'Average'), ('good', 'Good'), ('very good', 'Very Good')], default=None, max_length=30, null=True, verbose_name='Mood')),
                ('day_quality', models.CharField(blank=True, choices=[('very bad', 'Very Bad'), ('bad', 'Bad'), ('average', 'Average'), ('good', 'Good'), ('very good', 'Very Good')], default=None, max_length=30, null=True, verbose_name='Day Quality')),
                ('productivity', models.CharField(blank=True, choices=[('very bad', 'Very Bad'), ('bad', 'Bad'), ('average', 'Average'), ('good', 'Good'), ('very good', 'Very Good')], default=None, max_length=30, null=True, verbose_name='Productivity')),
                ('remarks', models.TextField(blank=True, default=None, null=True, verbose_name='Remarks')),
                ('astronaut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Astronaut')),
            ],
            options={
                'verbose_name': 'Mood Report',
                'verbose_name_plural': 'Mood Reports',
                'ordering': ['-datetime'],
            },
        ),
        migrations.CreateModel(
            name='Sleep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Location')),
                ('quality', models.CharField(blank=True, choices=[('very bad', 'Very Bad'), ('bad', 'Bad'), ('average', 'Average'), ('good', 'Good'), ('very good', 'Very Good')], default=None, max_length=30, null=True, verbose_name='Quality')),
                ('datetime_start', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start')),
                ('datetime_end', models.DateTimeField(blank=True, default=None, null=True, verbose_name='End')),
                ('duration', models.DurationField(blank=True, default=None, null=True, verbose_name='Duration')),
                ('astronaut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Astronaut')),
            ],
            options={
                'verbose_name': 'Sleep Log',
                'verbose_name_plural': 'Sleep Logbook',
                'ordering': ['-datetime_start'],
            },
        ),
    ]