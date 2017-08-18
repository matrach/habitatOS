# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 21:11
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0001_initial'),
        ('building', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('day', models.DateField(default=django.utils.timezone.now, verbose_name='Report About Day')),
                ('stress', models.CharField(choices=[('very-high', 'Very High'), ('high', 'High'), ('normal', 'Normal'), ('low', 'Low'), ('very-low', 'Very Low')], default=None, max_length=30, verbose_name='Stress')),
                ('mood', models.CharField(choices=[('very-high', 'Very High'), ('high', 'High'), ('normal', 'Normal'), ('low', 'Low'), ('very-low', 'Very Low')], default=None, max_length=30, verbose_name='Mood')),
                ('day_quality', models.CharField(choices=[('very-good', 'Very Good'), ('good', 'Good'), ('average', 'Average'), ('bad', 'Bad'), ('very-bad', 'Very Bad')], default=None, max_length=30, verbose_name='Day Quality')),
                ('productivity', models.CharField(choices=[('very-high', 'Very High'), ('high', 'High'), ('normal', 'Normal'), ('low', 'Low'), ('very-low', 'Very Low')], default=None, max_length=30, verbose_name='Productivity')),
                ('remarks', models.TextField(blank=True, default=None, verbose_name='Remarks')),
                ('astronaut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Astronaut')),
            ],
            options={
                'verbose_name': 'Mood Report',
                'verbose_name_plural': 'Mood Reports',
                'ordering': ['-day'],
            },
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Datetime')),
                ('communication_frequency', models.PositiveSmallIntegerField(choices=[(1, 'almost never'), (2, 'rarely'), (3, 'sometimes'), (4, 'moderately'), (5, 'rather often'), (6, 'very often'), (7, 'almost all the time')], verbose_name='How frequently do you communicate with following people?')),
                ('communication_desired', models.PositiveSmallIntegerField(choices=[(1, 'almost never'), (2, 'rarely'), (3, 'sometimes'), (4, 'moderately'), (5, 'rather often'), (6, 'very often'), (7, 'almost all the time')], verbose_name='How often do you want to communicate with following people?')),
                ('personal_preferences', models.PositiveSmallIntegerField(choices=[(1, 'I would rather avoid him/her'), (2, ''), (3, ''), (4, ''), (5, ''), (6, ''), (7, 'I would love to with with him/her all the time')], verbose_name='Personal preferences: Please, evaluate the following people according to your preference to interact with them in your free time.')),
                ('work_preferences', models.PositiveSmallIntegerField(choices=[(1, 'I would rather avoid him/her'), (2, ''), (3, ''), (4, ''), (5, ''), (6, ''), (7, 'I would love to with with him/her all the time')], verbose_name='Work preferences: Please, evaluate the following people according to your preference to work with them.')),
                ('communication_quality', models.PositiveSmallIntegerField(choices=[(1, 'should always be better'), (2, 'should often be better'), (3, 'should sometimes be better'), (4, 'sufficient'), (5, 'sometimes above average'), (6, 'often above average'), (7, 'always above average')], verbose_name='Evaluate the quality of communication with following people (taking into account its relevance, content, timeliness, etc.).')),
                ('know_already', models.PositiveSmallIntegerField(choices=[(1, 'not at all'), (2, 'not much'), (3, 'moderately'), (4, 'quite well'), (5, 'well'), (6, 'very well'), (7, 'perfectly well')], verbose_name='How well do you know the following people?')),
                ('know_desired', models.PositiveSmallIntegerField(choices=[(1, 'not at all'), (2, 'not much'), (3, 'moderately'), (4, 'quite well'), (5, 'well'), (6, 'very well'), (7, 'perfectly well')], verbose_name='How well do you want to know the following people?')),
                ('cooperation_quality', models.PositiveSmallIntegerField(choices=[(1, 'totally insufficient'), (2, 'often insufficient'), (3, 'sometimes insufficient'), (4, 'sufficient'), (5, 'rather high'), (6, 'high'), (7, 'excellent')], verbose_name='Evaluate the quality of cooperation with the following people?')),
                ('trust', models.PositiveSmallIntegerField(choices=[(1, 'Totally'), (2, 'Very much'), (3, 'A lot'), (4, 'Partly'), (5, 'A little'), (6, 'Not much'), (7, 'Not at all')], verbose_name='How much do you trust the following people?')),
                ('team_atmosphere', models.PositiveSmallIntegerField(choices=[(1, 'Terrible'), (2, ''), (3, ''), (4, ''), (5, ''), (6, ''), (7, 'Amazing')], verbose_name='How is the atmosphere within the team?')),
                ('team_misunderstandings', models.PositiveSmallIntegerField(choices=[(1, 'Never'), (2, ''), (3, ''), (4, ''), (5, ''), (6, ''), (7, 'Constantly')], verbose_name='Have there been any misunderstandings in the team?')),
                ('discomfort', models.TextField(verbose_name='If applicable, name the source(s) for the discomfort you are experience (e.g. noise, smell, food, sleeping problems, interpersonal conflict, etc.)')),
                ('remarks', models.TextField(verbose_name='You can add any comment or note (e.g. if something important happened, how do you feel etc.)')),
                ('astronaut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Astronaut')),
            ],
            options={
                'verbose_name': 'Questionnaire',
                'verbose_name_plural': 'Questionnaires',
                'ordering': ['-datetime'],
            },
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('size', models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('huge', 'Huge')], default=None, max_length=30, verbose_name='Problem Size')),
                ('status', models.CharField(choices=[('broken', 'Broken'), ('fixed', 'Fixed'), ('destroyed', 'Permanently Destroyed')], default=None, max_length=30, verbose_name='Current Status')),
                ('what', models.CharField(default=None, max_length=255, verbose_name='What')),
                ('start', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Start')),
                ('end', models.DateTimeField(blank=True, default=None, help_text='Leave empty if problem persists.', null=True, verbose_name='End')),
                ('duration', models.DurationField(blank=True, default=None, null=True, verbose_name='Duration')),
                ('description', models.TextField(blank=True, default=None, null=True, verbose_name='Description')),
                ('solution', models.TextField(blank=True, default=None, null=True, verbose_name='Solution')),
                ('location', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='building.Module', verbose_name='Location')),
                ('object', models.ForeignKey(blank=True, default=None, help_text='Leave empty, if object is not on the list', null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Item', verbose_name='Object')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Reporter')),
            ],
            options={
                'verbose_name': 'Repair',
                'verbose_name_plural': 'Repair Logbook',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Sleep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('type', models.CharField(choices=[('sleep', 'Sleep'), ('nap', 'Nap')], default=None, max_length=30, verbose_name='Type')),
                ('duration', models.DurationField(blank=True, default=None, null=True, verbose_name='Duration')),
                ('last_activity', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='What was the last thing you did before going to sleep?')),
                ('sleepy', models.CharField(blank=True, choices=[('no', 'No'), ('mildly', 'Mildly'), ('considerably', 'Considerably'), ('intensely', 'Intensely')], default=None, max_length=30, null=True, verbose_name='Did you feel sleepy during the day?')),
                ('sleepy_remarks', models.PositiveSmallIntegerField(blank=True, default=None, help_text='Percent of wake time', null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='If yes, how much?')),
                ('asleep_bedtime', models.DateTimeField(blank=True, default=None, null=True, verbose_name='When did you go to bed?')),
                ('asleep_time', models.DateTimeField(default=None, verbose_name='When did you fall asleep?')),
                ('asleep_problems', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='If it took you longer than 10 min to fall asleep, what was the reason?')),
                ('impediments_count', models.PositiveSmallIntegerField(blank=True, default=None, help_text='Minutes', null=True, verbose_name='Did you wake up at night? If you yes, for how long (approx.)?')),
                ('impediments_remarks', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='If you woke up during the night, why?')),
                ('wakeup_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='When did you wake up?')),
                ('wakeup_reasons', models.CharField(blank=True, default=None, help_text='Alarm clock / I woke up on my own', max_length=255, null=True, verbose_name='What woke you up in the morning?')),
                ('getup', models.DateTimeField(blank=True, default=None, null=True, verbose_name='When did you get up?')),
                ('aid_ear_plugs', models.NullBooleanField(choices=[(None, 'Undisclosed'), (True, 'Yes'), (False, 'No')], default=None, verbose_name='Did you use ear plugs?')),
                ('aid_eye_mask', models.NullBooleanField(choices=[(None, 'Undisclosed'), (True, 'Yes'), (False, 'No')], default=None, verbose_name='Did you use an eye mask?')),
                ('aid_pills', models.NullBooleanField(choices=[(None, 'Undisclosed'), (True, 'Yes'), (False, 'No')], default=None, verbose_name='Did you use a sleep pills?')),
                ('dream', models.TextField(blank=True, default=None, null=True, verbose_name='If you remember what was your dream about?')),
                ('sleep_amount', models.CharField(choices=[('sufficient', 'Sufficient'), ('slightly-sufficient', 'Slightly Sufficient'), ('somewhat-sufficient', 'Somewhat Sufficient'), ('very-insufficient', 'Very Insufficient')], default=None, max_length=30, verbose_name='How would you describe the amount of sleep?')),
                ('quality', models.CharField(choices=[('satisfactory', 'Satisfactory'), ('slightly-satisfactory', 'Slightly Satisfactory'), ('somewhat-satisfactory', 'Somewhat Satisfactory'), ('very-unsatisfactory', 'Very Unsatisfactory')], default=None, max_length=30, verbose_name='How would you rate your overall quality of sleep?')),
                ('astronaut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Astronaut')),
                ('location', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='building.Module', verbose_name='Location')),
            ],
            options={
                'verbose_name': 'Sleep Log',
                'verbose_name_plural': 'Sleep Logbook',
                'ordering': ['-asleep_bedtime'],
            },
        ),
    ]