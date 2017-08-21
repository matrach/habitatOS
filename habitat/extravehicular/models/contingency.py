from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel


class Contingency(HabitatModel):

    SEVERITY_EMERGENCY = 'emergency'
    SEVERITY_CRITICAL = 'critical'
    SEVERITY_WARNING = 'warning'
    SEVERITY_INFO = 'info'

    SEVERITY_CHOICES = [
        (SEVERITY_EMERGENCY, _('Emergency - ABORT the simulation')),
        (SEVERITY_CRITICAL, _('Critical - ABORT the EVA')),
        (SEVERITY_WARNING, _('Warning')),
        (SEVERITY_INFO, _('Informative')),
    ]

    identifier = models.CharField(
        verbose_name=_('Identifier'),
        max_length=10,
        unique=True)

    severity = models.CharField(
        verbose_name=_('Severity'),
        max_length=30,
        choices=SEVERITY_CHOICES,
        default=SEVERITY_INFO)

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=100,
        unique=True)

    description = models.TextField(
        verbose_name=_('Description'))

    recovery_procedure = models.TextField(
        verbose_name=_('Recovery Procedure'))

    remarks = models.TextField(
        verbose_name=_('Additional Remarks'),
        blank=True,
        null=True,
        default=None)

    @staticmethod
    def autocomplete_search_fields():
        return ['identifier__iexact', 'name__icontains']

    def __str__(self):
        return f'[{self.identifier}] {self.severity} {self.name}'

    class Meta:
        verbose_name = _('Contingency')
        verbose_name_plural = _('Contingencies')
