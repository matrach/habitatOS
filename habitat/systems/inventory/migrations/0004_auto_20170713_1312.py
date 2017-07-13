# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-13 13:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20170713_1312'),
        ('inventory', '0003_delete_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=None, max_length=7, verbose_name='Code')),
                ('quantity', models.PositiveSmallIntegerField(default=1, verbose_name='Quantity')),
                ('best_before', models.DateField(default=None, verbose_name='Best before')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Edible',
                'verbose_name_plural': 'Edibles Database',
                'ordering': ['code'],
            },
        ),
        migrations.AlterField(
            model_name='item',
            name='code',
            field=models.CharField(default=None, max_length=7, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default=None, max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Quantity'),
        ),
    ]