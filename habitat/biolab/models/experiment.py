from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now


class Experiment(models.Model):
    CULTIVATION_METHODS_SOIL = 'soil'
    CULTIVATION_METHODS_UNDERWATER = 'underwater'
    CULTIVATION_METHODS_ARTIFICIAL = 'artificial'
    CULTIVATION_METHODS_HYDROPONICS = 'hydroponics'
    CULTIVATION_METHODS_AEROPONICS = 'aeroponics'
    CULTIVATION_METHODS_MIXED = 'mixed'
    CULTIVATION_METHODS_OTHER = 'other'

    CULTIVATION_METHODS_CHOICES = [
        (CULTIVATION_METHODS_SOIL, _('Soil')),
        (CULTIVATION_METHODS_UNDERWATER, _('Underwater')),
        (CULTIVATION_METHODS_ARTIFICIAL, _('Artificial')),
        (CULTIVATION_METHODS_HYDROPONICS, _('Hydroponics')),
        (CULTIVATION_METHODS_AEROPONICS, _('Aeroponics')),
        (CULTIVATION_METHODS_MIXED, _('Mixed')),
        (CULTIVATION_METHODS_OTHER, _('Other'))
    ]

    plant = models.ForeignKey(verbose_name=_('Plant'), to='biolab.Plant')
    cultivation_method = models.CharField(verbose_name=_('Cultivation method'), choices=CULTIVATION_METHODS_CHOICES, max_length=30, default=None)
    planted_date = models.DateTimeField(verbose_name=_('Date Planted'), default=now)
    image = models.ImageField(verbose_name=_('Image'), blank=True, null=True, default=None)

    def __str__(self):
        return f'[{self.planted_date:%Y-%m-%d}] {self.plant} {self.cultivation_method}'

    class Meta:
        ordering = ['-planted_date']
        verbose_name = _('Experiment')
        verbose_name_plural = _('Experiments')
