# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 13:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notepad', '0002_auto_20170325_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalnote',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalnote',
            name='content',
            field=models.TextField(default=None, verbose_name='Content'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalnote',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=None, verbose_name='Datetime'),
            preserve_default=False,
        ),
    ]
