from django.contrib import admin
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now


class BloodPressure(models.Model):
    astronaut = models.ForeignKey(
        verbose_name=_('Astronaut'),
        to='auth.User',
        limit_choices_to={'groups__name': 'Astronauts'})

    datetime = models.DateTimeField(
        verbose_name=_('Datetime'),
        default=now)

    systolic = models.PositiveSmallIntegerField(
        verbose_name=_('Blood Pressure Systolic'),
        help_text=_('mmHg'),
        validators=[
            MaxValueValidator(250),
            MinValueValidator(0)])

    diastolic = models.PositiveSmallIntegerField(
        verbose_name=_('Blood Pressure Diastolic'),
        help_text=_('mmHg'),
        validators=[
            MaxValueValidator(250),
            MinValueValidator(0)])

    def __str__(self):
        return f'[{self.datetime:%Y-%m-%d %H:%M}] {self.astronaut} BP: {self.systolic}/{self.diastolic}'

    class Meta:
        ordering = ['-datetime']
        verbose_name = _('Blood Pressure Measurement')
        verbose_name = _('Blood Pressure Database')

    class Admin(admin.ModelAdmin):
        list_display = ['datetime', 'astronaut', 'systolic', 'diastolic']
        list_filter = ['astronaut']
