# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 14:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_public', models.BooleanField(default=True)),
                ('date_added', models.DateField(blank=True, null=True)),
                ('order', models.PositiveIntegerField(default=9999)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='reports/')),
                ('description', models.TextField(blank=True, null=True)),
                ('is_public', models.BooleanField(default=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.Album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='cover_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='reporting.Photo'),
        ),
    ]
