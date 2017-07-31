# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 18:41
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default=None, max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(default=None, editable=False, verbose_name='Slug')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='food.ProductCategory', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Product Category',
                'verbose_name_plural': 'Product Categories',
                'ordering': ['slug', 'name'],
            },
        ),
        migrations.CreateModel(
            name='ProductShoppingUnits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=None, verbose_name='Value')),
            ],
        ),
        migrations.CreateModel(
            name='ProductUsageUnits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=None, verbose_name='Value')),
            ],
        ),
        migrations.AddField(
            model_name='dayplan',
            name='tags',
            field=models.ManyToManyField(blank=True, default=None, to='food.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='product',
            name='modification_author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Modification Author'),
        ),
        migrations.AddField(
            model_name='product',
            name='modification_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Modification Date'),
        ),
        migrations.AddField(
            model_name='tag',
            name='type',
            field=models.CharField(choices=[('product', 'Product'), ('plan', 'Plan'), ('meal', 'Meal')], default='product', max_length=30, verbose_name='Type'),
        ),
        migrations.AddField(
            model_name='unit',
            name='type',
            field=models.CharField(choices=[('shopping', 'Shopping'), ('usage', 'Usage')], default='usage', max_length=30, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cooking_factor',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Cooking Factor'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cooking_product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='food.Product', verbose_name='From Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cooking_waste',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)], verbose_name='Cooking Waste'),
        ),
        migrations.AddField(
            model_name='productusageunits',
            name='unit',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='food.Unit', verbose_name='Unit'),
        ),
        migrations.AddField(
            model_name='productshoppingunits',
            name='unit',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='food.Unit', verbose_name='Unit'),
        ),
    ]
