from django.contrib import admin
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now


class BloodPressure(models.Model):
    astronaut = models.ForeignKey(
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

    class Meta:
        ordering = ['-datetime']

    class Admin(admin.ModelAdmin):
        list_display = ['datetime', 'systolic', 'diastolic']
