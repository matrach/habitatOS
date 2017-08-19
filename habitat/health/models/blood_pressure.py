from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime
from habitat._common.models import ReporterAstronaut


class BloodPressure(HabitatModel, MissionDateTime, ReporterAstronaut):

    systolic = models.PositiveSmallIntegerField(
        verbose_name=_('Blood Pressure Systolic'),
        help_text=_('mmHg'),
        default=None,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(250)])

    diastolic = models.PositiveSmallIntegerField(
        verbose_name=_('Blood Pressure Diastolic'),
        help_text=_('mmHg'),
        default=None,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(250)])

    heart_rate = models.PositiveSmallIntegerField(
        verbose_name=_('Heart Rate'),
        help_text=_('bpm'),
        default=None,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(250)])

    def __str__(self):
        return f'[{self.date} {self.time}] {self.reporter} BP: {self.systolic}/{self.diastolic}'

    class Meta:
        verbose_name = _('Blood Pressure')
        verbose_name_plural = _('Blood Pressure')
