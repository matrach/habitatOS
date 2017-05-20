from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.contrib import admin


class PulsOxymetry(models.Model):
    astronaut = models.ForeignKey(
        to='auth.User',
        limit_choices_to={'groups__name': 'Astronauts'})

    datetime = models.DateTimeField(
        verbose_name=_('Datetime'),
        default=now)

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
            MinValueValidator(0)])


    def __str__(self):
        return f'[{self.datetime}] {self.astronaut} SpO2: {self.spo2}, HR: {self.heart_rate}, PI: {self.perfusion_index}'

    class Meta:
        ordering = ['-datetime']

    class Admin(admin.ModelAdmin):
        list_display = ['datetime', 'astronaut', 'spo2', 'perfusion_index', 'heart_rate']
