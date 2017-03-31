from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class PulsOxymetry(models.Model):
    spo2 = models.PositiveSmallIntegerField(
        verbose_name=_('SpO2'),
        help_text=_('%'),
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])

    perfusion_index = models.DecimalField(
        verbose_name=_('Blood Perfusion Index'),
        decimal_places=1,
        max_digits=3,
        validators=[
            MaxValueValidator(22),
            MinValueValidator(0)
        ])

    heart_rate = models.PositiveSmallIntegerField(
        verbose_name=_('Heart Rate'),
        help_text=_('bpm'),
        validators=[
            MaxValueValidator(250),
            MinValueValidator(0)
        ])
