from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime
from habitat._common.models import ReporterAstronaut


class SociodynamicReportEntry(HabitatModel):
    report = models.ForeignKey(verbose_name=_('Report'), to='reporting.SociodynamicReport')
    astronaut = models.ForeignKey(verbose_name=_('Astronaut'), to='auth.User', limit_choices_to={'groups__name': 'Astronauts'})
    impression = models.TextField(verbose_name=_('Astronaut X is...'), blank=True, null=True, default=None)
    like = models.TextField(verbose_name=_('I like about him/her...'), blank=True, null=True, default=None)
    dislike = models.TextField(verbose_name=_('I do not like about him/her...'), blank=True, null=True, default=None)


class SociodynamicReport(HabitatModel, MissionDateTime, ReporterAstronaut):

    def __str__(self):
        return f'[{self.date}] {self.reporter}'

    class Meta:
        verbose_name = _('Sociodynamic Report')
        verbose_name_plural = _('Sociodynamics')
