from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime
from habitat._common.models import ReporterAstronaut


class Communication(HabitatModel, MissionDateTime, ReporterAstronaut):

    communication_frequency = models.PositiveSmallIntegerField(
        verbose_name=_('How frequently do you communicate with following people?'),
        choices=[
            (1, _('almost never')),
            (2, _('rarely')),
            (3, _('sometimes')),
            (4, _('moderately')),
            (5, _('rather often')),
            (6, _('very often')),
            (7, _('almost all the time'))])

    communication_desired = models.PositiveSmallIntegerField(
        verbose_name=_('How often do you want to communicate with following people?'),
        choices=[
            (1, _('almost never')),
            (2, _('rarely')),
            (3, _('sometimes')),
            (4, _('moderately')),
            (5, _('rather often')),
            (6, _('very often')),
            (7, _('almost all the time'))])

    personal_preferences = models.PositiveSmallIntegerField(
        verbose_name=_('Personal preferences: Please, evaluate the following people according to your preference to interact with them in your free time.'),
        choices=[
            (1, _('I would rather avoid him/her')),
            (2, ''),
            (3, ''),
            (4, ''),
            (5, ''),
            (6, ''),
            (7, _('I would love to with with him/her all the time'))])

    work_preferences = models.PositiveSmallIntegerField(
        verbose_name=_('Work preferences: Please, evaluate the following people according to your preference to work with them.'),
        choices=[
            (1, _('I would rather avoid him/her')),
            (2, ''),
            (3, ''),
            (4, ''),
            (5, ''),
            (6, ''),
            (7, _('I would love to with with him/her all the time'))])

    communication_quality = models.PositiveSmallIntegerField(
        verbose_name=_('Evaluate the quality of communication with following people (taking into account its relevance, content, timeliness, etc.).'),
        choices=[
            (1, _('should always be better')),
            (2, _('should often be better')),
            (3, _('should sometimes be better')),
            (4, _('sufficient')),
            (5, _('sometimes above average')),
            (6, _('often above average')),
            (7, _('always above average'))])

    know_already = models.PositiveSmallIntegerField(
        verbose_name=_('How well do you know the following people?'),
        choices=[
            (1, _('not at all')),
            (2, _('not much')),
            (3, _('moderately')),
            (4, _('quite well')),
            (5, _('well')),
            (6, _('very well')),
            (7, _('perfectly well'))])

    know_desired = models.PositiveSmallIntegerField(
        verbose_name=_('How well do you want to know the following people?'),
        choices=[
            (1, _('not at all')),
            (2, _('not much')),
            (3, _('moderately')),
            (4, _('quite well')),
            (5, _('well')),
            (6, _('very well')),
            (7, _('perfectly well'))])

    cooperation_quality = models.PositiveSmallIntegerField(
        verbose_name=_('Evaluate the quality of cooperation with the following people?'),
        choices=[
            (1, _('totally insufficient')),
            (2, _('often insufficient')),
            (3, _('sometimes insufficient')),
            (4, _('sufficient')),
            (5, _('rather high')),
            (6, _('high')),
            (7, _('excellent'))])

    trust = models.PositiveSmallIntegerField(
        verbose_name=_('How much do you trust the following people?'),
        choices=[
            (1, _('Totally')),
            (2, _('Very much')),
            (3, _('A lot')),
            (4, _('Partly')),
            (5, _('A little')),
            (6, _('Not much')),
            (7, _('Not at all'))])

    team_atmosphere = models.PositiveSmallIntegerField(
        verbose_name=_('How is the atmosphere within the team?'),
        choices=[
            (1, _('Terrible')),
            (2, ''),
            (3, ''),
            (4, ''),
            (5, ''),
            (6, ''),
            (7, _('Amazing'))])

    team_misunderstandings = models.PositiveSmallIntegerField(
        verbose_name=_('Have there been any misunderstandings in the team?'),
        choices=[
            (1, _('Never')),
            (2, ''),
            (3, ''),
            (4, ''),
            (5, ''),
            (6, ''),
            (7, _('Constantly'))])

    discomfort = models.TextField(
        verbose_name=_('If applicable, name the source(s) for the discomfort you are experience (e.g. noise, smell, food, sleeping problems, interpersonal conflict, etc.)'))

    remarks = models.TextField(
        verbose_name=_('You can add any comment or note (e.g. if something important happened, how do you feel etc.)'))

    def __str__(self):
        return f'[{self.date}] {self.reporter}'

    class Meta:
        verbose_name = _('Psychological')
        verbose_name_plural = _('Psychological')
