from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now


class Radiation(models.Model):

    datetime = models.DateTimeField(
        verbose_name=_('Datetime'),
        default=now)

    location = models.ForeignKey(
        verbose_name=_('Sensor Location'),
        to='building.Module',
        null=True,
        blank=True,
        default=None)

    value = models.DecimalField(
        verbose_name=_('Radiation'),
        help_text=_('Sievert'),
        max_digits=6,
        decimal_places=5,
        default=None)

    def __str__(self):
        return f'[{self.datetime:%Y-%m-%d %H:%M}] (location: {self.location}) {self.value} Sv'

    class Meta:
        ordering = ['-datetime', 'location']
        verbose_name = _('Radiation Measurement')
        verbose_name_plural = _('Radiation')

    class Admin(admin.ModelAdmin):
        change_list_template = 'admin/change_list_filter_sidebar.html'
        list_display = ['datetime', 'location', 'value']
        list_filter = ['location']
        search_fields = ['^datetime', 'value']