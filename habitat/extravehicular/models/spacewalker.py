from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel


class Spacewalker(HabitatModel):
    DESIGNATION_LEADER = 'leader'
    DESIGNATION_SUPPORT = 'support'

    DESIGNATION_CHOICES = [
        (DESIGNATION_LEADER, _('Lead Spacewalker')),
        (DESIGNATION_SUPPORT, _('Supporting Spacewalker')),
    ]

    activity = models.ForeignKey(
        verbose_name=_('Activity'),
        to='extravehicular.Activity')

    designation = models.CharField(
        verbose_name=_('Designation'),
        max_length=30,
        choices=DESIGNATION_CHOICES)

    participant = models.ForeignKey(
        verbose_name=_('Participant'),
        to='auth.User',
        limit_choices_to={'groups__name': 'Astronauts'})

    def __str__(self):
        return f'[{self.activity}] {self.designation} {self.participant}'

    class Meta:
        verbose_name = _('Spacewalker')
        verbose_name_plural = _('Spacewalkers')
