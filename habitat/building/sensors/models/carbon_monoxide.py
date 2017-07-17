from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator


class CarbonMonoxide(models.Model):

    datetime = models.DateTimeField(
        verbose_name=_('Datetime'),
        default=now)

    value = models.PositiveSmallIntegerField(
        verbose_name=_('Concentration'),
        help_text=_('%'),
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)])

    def __str__(self):
        return f'[{self.datetime}] {self.value}%'

    class Meta:
        ordering = ['-datetime']
        verbose_name = _('Carbon Monoxide Concentration Measurement')
        verbose_name_plural = _('Carbon Monoxide')

    class Admin(admin.ModelAdmin):
        list_display = ['datetime', 'value']
        search_fields = ['value']