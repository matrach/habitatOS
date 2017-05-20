# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychology', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='closedquestion',
            name='questionary',
        ),
        migrations.RemoveField(
            model_name='openquestion',
            name='questionary',
        ),
        migrations.RemoveField(
            model_name='userreponse',
            name='questionary',
        ),
        migrations.AddField(
            model_name='questionary',
            name='communication_desired',
            field=models.PositiveSmallIntegerField(choices=[(1, 'almost never'), (2, 'rarely'), (3, 'sometimes'), (4, 'moderately'), (5, 'rather often'), (6, 'very often'), (7, 'almost all the time')], default=None, verbose_name='How often do you want to communicate with following people?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionary',
            name='communication_frequency',
            field=models.PositiveSmallIntegerField(choices=[(1, 'almost never'), (2, 'rarely'), (3, 'sometimes'), (4, 'moderately'), (5, 'rather often'), (6, 'very often'), (7, 'almost all the time')], default=None, verbose_name='How frequently do you communicate with following people?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionary',
            name='communication_quality',
            field=models.PositiveSmallIntegerField(choices=[(1, 'should always be better'), (2, 'should often be better'), (3, 'should sometimes be better'), (4, 'sufficient'), (5, 'sometimes above average'), (6, 'often above average'), (7, 'always above average')], default=None, verbose_name='Evaluate the quality of communication with following people (taking into account its relevance, content, timeliness, etc.).'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionary',
            name='cooperation_quality',
            field=models.PositiveSmallIntegerField(choices=[(1, 'totally insufficient'), (2, 'often insufficient'), (3, 'sometimes insufficient'), (4, 'sufficient'), (5, 'rather high'), (6, 'high'), (7, 'excellent')], default=None, verbose_name='Evaluate the quality of cooperation with the following people?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionary',
            name='discomfort',
            field=models.TextField(default=None, verbose_name='If applicable, name the source(s) for the discomfort you are experience (e.g. noise, smell, food, sleeping problems, interpersonal conflict, etc.)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionary',
            name='know_already',
            field=models.PositiveSmallIntegerField(choices=[(1, 'not at all'), (2, 'not much'), (3, 'moderately'), (4, 'quite well'), (5, 'well'), (6, 'very well'), (7, 'perfectly well')], default=None, verbose_name='How well do you know the following people?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionary',
            name='know_desired',
            field=models.PositiveSmallIntegerField(choices=[(1, 'not at all'), (2, 'not much'), (3, 'moderately'), (4, 'quite well'), (5, 'well'), (6, 'very well'), (7, 'perfectly well')], default=None, verbose_name='How well do you want to know the following people?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionary',
            name='personal_preferences',
            field=models.PositiveSmallIntegerField(choices=[(1, 'I would rather avoid him/her'), (2, ''), (3, ''), (4, ''), (5, ''), (6, ''), (7, 'I would love to with with him/her all the time')], default=None, verbose_name='Personal preferences: Please, evaluate the following people according to your preference to interact with them in your free time.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionary',
            name='remarks',
            field=models.TextField(default=None, verbose_name='You can add any comment or note (e.g. if something important happened, how do you feel etc.)\u2028'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionary',
            name='team_atmosphere',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Terrible'), (2, ''), (3, ''), (4, ''), (5, ''), (6, ''), (7, 'Amazing')], default=None, verbose_name='How is the atmosphere within the team?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionary',
            name='team_misunderstandings',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Never'), (2, ''), (3, ''), (4, ''), (5, ''), (6, ''), (7, 'Constantly')], default=None, verbose_name='Have there been any misunderstandings in the team?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionary',
            name='trust',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Totally'), (2, 'Very much'), (3, 'A lot'), (4, 'Partly'), (5, 'A little'), (6, 'Not much'), (7, 'Not at all')], default=None, verbose_name='How much do you trust the following people?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionary',
            name='work_preferences',
            field=models.PositiveSmallIntegerField(choices=[(1, 'I would rather avoid him/her'), (2, ''), (3, ''), (4, ''), (5, ''), (6, ''), (7, 'I would love to with with him/her all the time')], default=None, verbose_name='Work preferences: Please, evaluate the following people according to your preference to work with them.'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ClosedQuestion',
        ),
        migrations.DeleteModel(
            name='OpenQuestion',
        ),
        migrations.DeleteModel(
            name='UserReponse',
        ),
    ]