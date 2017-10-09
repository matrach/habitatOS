from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel


class Spacewalker(HabitatModel):
    DESIGNATION_EV_LEADER = 'ev-leader'
    DESIGNATION_EV_SUPPORT = 'ev-support'
    DESIGNATION_HABITAT_SUPPORT = 'habitat-support'
    DESIGNATION_ROVER_OPERATOR = 'rover-operator'

    DESIGNATION_CHOICES = [
        (DESIGNATION_EV_LEADER, _('Lead Spacewalker')),
        (DESIGNATION_EV_SUPPORT, _('Supporting Spacewalker')),
        (DESIGNATION_HABITAT_SUPPORT, _('Habitat Support')),
        (DESIGNATION_ROVER_OPERATOR, _('Rover Operator')),
    ]

    activity = models.ForeignKey(
        verbose_name=_('Activity'),
        to='extravehicular.Activity')

    participant = models.ForeignKey(
        verbose_name=_('Participant'),
        to='auth.User',
        limit_choices_to={'groups__name': 'Astronauts'})

    designation = models.CharField(
        verbose_name=_('Designation'),
        max_length=30,
        choices=DESIGNATION_CHOICES)

    medicals_before = models.TextField(
        verbose_name=_('Medicals Before EVA'),
        blank=True,
        null=True,
        default=None)

    medicals_after = models.TextField(
        verbose_name=_('Medicals After EVA'),
        blank=True,
        null=True,
        default=None)

    def __str__(self):
        return f'[{self.activity}] {self.designation} {self.participant}'

    class Meta:
        verbose_name = _('Spacewalker')
        verbose_name_plural = _('Spacewalkers')
