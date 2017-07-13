# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 22:55
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicine', '0008_auto_20170520_2150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meal',
            options={'ordering': ['-datetime']},
        ),
        migrations.AlterModelOptions(
            name='qualityoflife',
            options={'ordering': ['-datetime']},
        ),
        migrations.AddField(
            model_name='meal',
            name='astronaut',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Astronaut'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meal',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Datetime'),
        ),
        migrations.AddField(
            model_name='meal',
            name='food',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Food'),
        ),
        migrations.AddField(
            model_name='qualityoflife',
            name='astronaut',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Astronaut'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qualityoflife',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Datetime'),
        ),
        migrations.AddField(
            model_name='qualityoflife',
            name='day_quality',
            field=models.CharField(blank=True, choices=[('very bad', 'Very Bad'), ('bad', 'Bad'), ('average', 'Average'), ('good', 'Good'), ('very good', 'Very Good')], default=None, max_length=30, null=True, verbose_name='Space Work'),
        ),
        migrations.AddField(
            model_name='qualityoflife',
            name='day_summary',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Day Summary'),
        ),
        migrations.AddField(
            model_name='qualityoflife',
            name='evening_mood',
            field=models.CharField(blank=True, choices=[('very bad', 'Very Bad'), ('bad', 'Bad'), ('average', 'Average'), ('good', 'Good'), ('very good', 'Very Good')], default=None, max_length=30, null=True, verbose_name='Evening Mood'),
        ),
        migrations.AddField(
            model_name='qualityoflife',
            name='evening_stress',
            field=models.CharField(blank=True, choices=[('very bad', 'Very Bad'), ('bad', 'Bad'), ('average', 'Average'), ('good', 'Good'), ('very good', 'Very Good')], default=None, max_length=30, null=True, verbose_name='Evening Stress'),
        ),
        migrations.AddField(
            model_name='qualityoflife',
            name='morning_mood',
            field=models.CharField(blank=True, choices=[('very bad', 'Very Bad'), ('bad', 'Bad'), ('average', 'Average'), ('good', 'Good'), ('very good', 'Very Good')], default=None, max_length=30, null=True, verbose_name='Morning Mood'),
        ),
        migrations.AddField(
            model_name='qualityoflife',
            name='morning_stress',
            field=models.CharField(blank=True, choices=[('very bad', 'Very Bad'), ('bad', 'Bad'), ('average', 'Average'), ('good', 'Good'), ('very good', 'Very Good')], default=None, max_length=30, null=True, verbose_name='Morning Stress'),
        ),
        migrations.AddField(
            model_name='qualityoflife',
            name='productivity',
            field=models.CharField(blank=True, choices=[('very bad', 'Very Bad'), ('bad', 'Bad'), ('average', 'Average'), ('good', 'Good'), ('very good', 'Very Good')], default=None, max_length=30, null=True, verbose_name='Productivity'),
        ),
        migrations.AddField(
            model_name='qualityoflife',
            name='space_work',
            field=models.CharField(blank=True, choices=[('very bad', 'Very Bad'), ('bad', 'Bad'), ('average', 'Average'), ('good', 'Good'), ('very good', 'Very Good')], default=None, max_length=30, null=True, verbose_name='Space Work'),
        ),
        migrations.AddField(
            model_name='weight',
            name='body_fat',
            field=models.DecimalField(decimal_places=1, default=None, help_text='%', max_digits=3, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='Body Fat', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='weight',
            name='body_water',
            field=models.DecimalField(decimal_places=1, default=None, help_text='kg', max_digits=4, validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(0)], verbose_name='Body Water',null=True, blank=True),
        ),
        migrations.AddField(
            model_name='weight',
            name='bone_mass',
            field=models.DecimalField(decimal_places=1, default=None, help_text='kg', max_digits=4, validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(0)], verbose_name='Bone Mass', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='weight',
            name='daily_caloric_intake',
            field=models.PositiveIntegerField(default=None, help_text='kcal', validators=[django.core.validators.MaxValueValidator(4000), django.core.validators.MinValueValidator(0)], verbose_name='Daily Caloric Intake', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='weight',
            name='lean_body_mass',
            field=models.DecimalField(decimal_places=1, default=None, help_text='%', max_digits=4, validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(0)], verbose_name='Lean Body Mass', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='weight',
            name='muscle_mass',
            field=models.DecimalField(decimal_places=1, default=None, help_text='kg', max_digits=4, validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(0)], verbose_name='Muscle Mass', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='weight',
            name='visceral_fat',
            field=models.PositiveSmallIntegerField(default=None, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Visceral Fat', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='bloodpressure',
            name='astronaut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Astronaut'),
        ),
        migrations.AlterField(
            model_name='disease',
            name='astronaut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Astronaut'),
        ),
        migrations.AlterField(
            model_name='disease',
            name='datetime_end',
            field=models.DateTimeField(default=None, verbose_name='End Datetime'),
        ),
        migrations.AlterField(
            model_name='disease',
            name='icd10',
            field=models.CharField(default=None, max_length=50, verbose_name='ICD-10'),
        ),
        migrations.AlterField(
            model_name='disease',
            name='sympthoms',
            field=models.TextField(default=None, verbose_name='Sympthoms'),
        ),
        migrations.AlterField(
            model_name='pulsoxymetry',
            name='astronaut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Astronaut'),
        ),
        migrations.AlterField(
            model_name='pulsoxymetry',
            name='heart_rate',
            field=models.PositiveSmallIntegerField(default=None, help_text='bpm', validators=[django.core.validators.MaxValueValidator(250), django.core.validators.MinValueValidator(0)], verbose_name='Heart Rate'),
        ),
        migrations.AlterField(
            model_name='pulsoxymetry',
            name='perfusion_index',
            field=models.DecimalField(decimal_places=1, default=None, max_digits=3, validators=[django.core.validators.MaxValueValidator(22), django.core.validators.MinValueValidator(0)], verbose_name='Blood Perfusion Index'),
        ),
        migrations.AlterField(
            model_name='pulsoxymetry',
            name='spo2',
            field=models.PositiveSmallIntegerField(default=None, help_text='%', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='SpO2'),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='astronaut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Astronaut'),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='astronaut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Astronaut'),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='temperature',
            field=models.DecimalField(decimal_places=1, default=None, help_text='Celsius', max_digits=3, validators=[django.core.validators.MaxValueValidator(42), django.core.validators.MinValueValidator(30)], verbose_name='Temperature'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='BMI',
            field=models.DecimalField(decimal_places=1, default=None, max_digits=3, validators=[django.core.validators.MaxValueValidator(40), django.core.validators.MinValueValidator(10)], verbose_name='BMI'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='astronaut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Astronaut'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='weight',
            field=models.DecimalField(decimal_places=1, default=None, help_text='kg', max_digits=4, validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(0)], verbose_name='Weight'),
        ),
    ]