from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime
from habitat._common.models import ReporterAstronaut


class Weight(HabitatModel, MissionDateTime, ReporterAstronaut):
    weight = models.DecimalField(
        verbose_name=_('Weight'),
        help_text=_('kg'),
        max_digits=4,
        decimal_places=1,
        default=None,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(200)])

    BMI = models.DecimalField(
        verbose_name=_('BMI'),
        max_digits=3,
        decimal_places=1,
        default=None,
        blank=True,
        null=True,
        validators=[
            MinValueValidator(10),
            MaxValueValidator(40)])

    body_fat = models.DecimalField(
        verbose_name=_('Body Fat'),
        help_text=_('%'),
        max_digits=3,
        decimal_places=1,
        default=None,
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)])

    lean_body_mass = models.DecimalField(
        verbose_name=_('Lean Body Mass'),
        help_text=_('%'),
        max_digits=4,
        decimal_places=1,
        default=None,
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(200)])

    body_water = models.DecimalField(
        verbose_name=_('Body Water'),
        help_text=_('kg'),
        max_digits=4,
        decimal_places=1,
        default=None,
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(200),
            MinValueValidator(0)])

    muscle_mass = models.DecimalField(
        verbose_name=_('Muscle Mass'),
        help_text=_('kg'),
        max_digits=4,
        decimal_places=1,
        default=None,
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(200)])

    daily_caloric_intake = models.PositiveIntegerField(
        verbose_name=_('Daily Caloric Intake'),
        help_text=_('kcal'),
        default=None,
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(4000)])

    bone_mass = models.DecimalField(
        verbose_name=_('Bone Mass'),
        help_text=_('kg'),
        max_digits=4,
        decimal_places=1,
        default=None,
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(200)])

    visceral_fat = models.PositiveSmallIntegerField(
        verbose_name=_('Visceral Fat'),
        default=None,
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)])

    def save(self, **kwargs):
        return super().save(**kwargs)

    def __str__(self):
        return f'[{self.date} {self.time}] {self.reporter} Weight: {self.weight}kg, BMI: {self.BMI}'

    class Meta:
        verbose_name = _('Weight')
        verbose_name_plural = _('Weight')
