# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 14:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0005_auto_20170717_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sleep',
            name='aid_ear_plugs',
            field=models.NullBooleanField(choices=[(None, 'Undisclosed'), (True, 'Yes'), (False, 'No')], default=None, verbose_name='Did you use ear plugs?'),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='aid_eye_mask',
            field=models.NullBooleanField(choices=[(None, 'Undisclosed'), (True, 'Yes'), (False, 'No')], default=None, verbose_name='Did you use an eye mask?'),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='aid_pills',
            field=models.NullBooleanField(choices=[(None, 'Undisclosed'), (True, 'Yes'), (False, 'No')], default=None, verbose_name='Did you use a sleep pills?'),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='asleep_bedtime',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='When did you go to bed?'),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='asleep_time',
            field=models.DateTimeField(default=None, verbose_name='When did you fall asleep?'),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='location',
            field=models.ForeignKey(default={'name': 'Dormitory'}, on_delete=django.db.models.deletion.CASCADE, to='modules.Module', verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='quality',
            field=models.CharField(choices=[('satisfactory', 'Satisfactory'), ('slightly-satisfactory', 'Slightly Satisfactory'), ('somewhat-satisfactory', 'Somewhat Satisfactory'), ('very-unsatisfactory', 'Very Unsatisfactory')], default=None, max_length=30, verbose_name='How would you rate your overall quality of sleep?'),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='sleep_amount',
            field=models.CharField(choices=[('sufficient', 'Sufficient'), ('slightly-sufficient', 'Slightly Sufficient'), ('somewhat-sufficient', 'Somewhat Sufficient'), ('very-insufficient', 'Very Insufficient')], default=None, max_length=30, verbose_name='How would you describe the amount of sleep?'),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='sleepy',
            field=models.CharField(blank=True, choices=[('no', 'No'), ('mildly', 'Mildly'), ('considerably', 'Considerably'), ('intensely', 'Intensely')], default=None, max_length=30, null=True, verbose_name='Did you feel sleepy during the day?'),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='wakeup_reasons',
            field=models.CharField(blank=True, default=None, help_text='Alarm clock / I woke up on my own', max_length=255, null=True, verbose_name='What woke you up in the morning?'),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='wakeup_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='When did you wake up?'),
        ),
    ]
