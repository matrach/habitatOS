from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.utils.timezone import now


class Luminance(models.Model):

    datetime = models.DateTimeField(
        verbose_name=_('Datetime'),
        default=now)

    value = models.PositiveSmallIntegerField(
        verbose_name=_('Luminance'),
        help_text=_('lumen'),
        default=None)

    def __str__(self):
        return f'[{self.datetime:%Y-%m-%d %H:%M}] {self.value} lumen'

    class Meta:
        ordering = ['-value']
        verbose_name = _('Luminance Measurement')
        verbose_name_plural = _('Luminance')

    class Admin(admin.ModelAdmin):
        list_display = ['datetime', 'value']
        search_fields = ['value']
