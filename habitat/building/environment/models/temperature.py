from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Temperature(models.Model):
    UNITS = [
        ('celsius', _('Celsius')),
        ('kelvin', _('Kelvin')),
        ('fahrenheit', _('Fahrenheit'))]

    value = models.PositiveSmallIntegerField(verbose_name=_('Temperature'))
    unit = models.CharField(verbose_name=_('Unit'), max_length=10, choices=UNITS, default='celsius')

    def __str__(self):
        return f'{self.value} {self.unit.upper():.1}'

    class Meta:
        ordering = ['-value']

    class Admin(admin.ModelAdmin):
        list_display = ['value', 'unit']
        search_fields = ['value']
