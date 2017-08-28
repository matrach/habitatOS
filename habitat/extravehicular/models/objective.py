from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel


class Objective(HabitatModel):

    identifier = models.CharField(
        verbose_name=_('Identifier'),
        max_length=10,
        unique=True)

    location = models.ForeignKey(
        verbose_name=_('Location'),
        to='extravehicular.Location',
        null=True,
        blank=True,
        default=None)

    estimated_duration = models.DurationField(
        verbose_name=_('Estimated Duration'),
        blank=True,
        null=True,
        default=None)

    objective = models.TextField(
        verbose_name=_('Objective'))

    remarks = models.TextField(
        verbose_name=_('Additional Remarks'))

    def __str__(self):
        return f'[{self.identifier}] (location: {self.location}) {self.objective:.30}'

    class Meta:
        verbose_name = _('Objective')
        verbose_name_plural = _('Objectives')
