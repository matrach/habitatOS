from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.contrib import admin


class Weight(models.Model):
    astronaut = models.ForeignKey(
        verbose_name=_('Astronaut'),
        to='auth.User',
        limit_choices_to={'groups__name': 'Astronauts'})

    datetime = models.DateTimeField(
        verbose_name=_('Datetime'),
        default=now)

    weight = models.DecimalField(
        verbose_name=_('Weight'),
        help_text=_('kg'),
        max_digits=4,
        decimal_places=1,
        default=None,
        validators=[
            MaxValueValidator(200),
            MinValueValidator(0)])

    BMI = models.DecimalField(
        verbose_name=_('BMI'),
        max_digits=3,
        decimal_places=1,
        default=None,
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(40),
            MinValueValidator(10)])

    body_fat = models.DecimalField(
        verbose_name=_('Body Fat'),
        help_text=_('%'),
        max_digits=3,
        decimal_places=1,
        default=None,
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)])

    lean_body_mass = models.DecimalField(
        verbose_name=_('Lean Body Mass'),
        help_text=_('%'),
        max_digits=4,
        decimal_places=1,
        default=None,
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(200),
            MinValueValidator(0)])

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
            MaxValueValidator(200),
            MinValueValidator(0)])

    daily_caloric_intake = models.PositiveIntegerField(
        verbose_name=_('Daily Caloric Intake'),
        help_text=_('kcal'),
        default=None,
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(4000),
            MinValueValidator(0)])

    bone_mass = models.DecimalField(
        verbose_name=_('Bone Mass'),
        help_text=_('kg'),
        max_digits=4,
        decimal_places=1,
        default=None,
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(200),
            MinValueValidator(0)])

    visceral_fat = models.PositiveSmallIntegerField(
        verbose_name=_('Visceral Fat'),
        default=None,
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)])

    def save(self, **kwargs):
        # self.BMI = self.weight / (height ** 2)
        return super().save(**kwargs)

    def __str__(self):
        return f'[{self.datetime:%Y-%m-%d %H:%M}] {self.astronaut} Weight: {self.weight}kg, BMI: {self.BMI}'

    class Meta:
        ordering = ['-datetime']
        verbose_name = _('Weight')
        verbose_name_plural = _('Weight')
