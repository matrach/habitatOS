from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime
from habitat._common.models import ReporterAstronaut


class PulseOxymetry(HabitatModel, MissionDateTime, ReporterAstronaut):

    spo2 = models.PositiveSmallIntegerField(
        verbose_name=_('SpO2'),
        help_text=_('%'),
        default=None,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)])

    perfusion_index = models.DecimalField(
        verbose_name=_('Blood Perfusion Index'),
        decimal_places=1,
        max_digits=3,
        default=None,
        validators=[
            MaxValueValidator(22),
            MinValueValidator(0)])

    heart_rate = models.PositiveSmallIntegerField(
        verbose_name=_('Heart Rate'),
        help_text=_('bpm'),
        default=None,
        validators=[
            MaxValueValidator(250),
            MinValueValidator(0)])

    def __str__(self):
        return f'[{self.date} {self.time}] {self.reporter} SpO2: {self.spo2}, HR: {self.heart_rate}, PI: {self.perfusion_index}'

    class Meta:
        verbose_name = _('Pulse Oxymetry')
        verbose_name_plural = _('Pulse Oxymetry')
