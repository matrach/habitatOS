from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.utils.timezone import now


class Luminance(models.Model):

    datetime = models.DateTimeField(
        verbose_name=_('Datetime'),
        default=now)

    location = models.ForeignKey(
        verbose_name=_('Sensor Location'),
        to='building.Module',
        null=True,
        blank=True,
        default=None)

    value = models.PositiveSmallIntegerField(
        verbose_name=_('Luminance'),
        help_text=_('lumen'),
        default=None)

    def __str__(self):
        return f'[{self.datetime:%Y-%m-%d %H:%M}] (location: {self.location}) {self.value} lumen'

    class Meta:
        ordering = ['-datetime', 'location']
        verbose_name = _('Luminance Measurement')
        verbose_name_plural = _('Luminance')

    class Admin(admin.ModelAdmin):
        change_list_template = 'admin/change_list_filter_sidebar.html'
        list_display = ['datetime', 'location', 'value']
        list_filter = ['location']
        search_fields = ['^datetime', 'value']
