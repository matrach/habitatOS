from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime
from habitat._common.models import ReporterAnyone


class Incident(HabitatModel, MissionDateTime, ReporterAnyone):
    TYPE_BIOHAZARD = 'biohazard'
    TYPE_ENVIRONMENTAL = 'environmental'
    TYPE_SECURITY = 'security'

    TYPE_CHOICES = [
        (TYPE_BIOHAZARD, _('Biohazard')),
        (TYPE_ENVIRONMENTAL, _('Environmental')),
        (TYPE_SECURITY, _('Security')),
    ]

    SEVERITY_EMERGENCY = 'emergency'
    SEVERITY_CRITICAL = 'critical'
    SEVERITY_WARNING = 'warning'
    SEVERITY_INFO = 'info'

    SEVERITY_CHOICES = [
        (SEVERITY_EMERGENCY, _('Emergency - ABORT the simulation')),
        (SEVERITY_CRITICAL, _('Critical')),
        (SEVERITY_WARNING, _('Warning')),
        (SEVERITY_INFO, _('Informative')),
    ]

    start = models.DateTimeField(
        verbose_name=_('Start Datetime'),
        default=now)

    end = models.DateTimeField(
        verbose_name=_('End Datetime'),
        default=now)

    location = models.ForeignKey(
        verbose_name=_('Location'),
        to='building.Module',
        null=True,
        blank=True,
        default=None)

    severity = models.CharField(
        verbose_name=_('Severity'),
        max_length=30,
        choices=SEVERITY_CHOICES,
        default=SEVERITY_INFO)

    subject = models.CharField(
        verbose_name=_('Subject'),
        max_length=100,
        default=None)

    description = models.TextField(
        verbose_name=_('Description'),
        blank=True,
        null=True,
        default=None)

    def __str__(self):
        return f'[{self.date} {self.time}] {self.location}: {self.subject}'

    class Meta:
        verbose_name = _('Incident')
        verbose_name_plural = _('Incident')
