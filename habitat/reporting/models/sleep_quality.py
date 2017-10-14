from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel


class SleepQuality(HabitatModel):
    """
    1 - Interrupted sleep caused by  nightmares or psychological issues (stress, anxiousness, homesickness, etc...)
    2 - Interrupted sleep caused by somatic pain of the body or need to go to the toilet
    3 - Interrupted sleep caused by external disturbances such noises, lights, insects
    4 - Interrupted sleep caused by too low or too high temperature
    5 - Interrupted sleep caused by hunger
    6 - Un-interrupted sleep without dreams (subject does not remember any dreams)
    7 - Un-interrupted sleep with dreams in black and white
    8 - Un-interrupted sleep with colorful dreams
    9 - Un-interrupted sleep with colorful dreams and detectable smells
    10 - Un-interrupted sleep with colorful dreams and detectable smells, flavours and tactile impressions  (like reality)
    """
    name = models.CharField(verbose_name=_('Name'), max_length=255, blank=None, null=None, default=None)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        verbose_name = _('Sleep Quality')
        verbose_name_plural = _('Sleep Qualities')
