from django.contrib import admin
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now


class Pressure(models.Model):

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
        verbose_name=_('Pressure'),
        help_text=_('mmHg'),
        max_digits=6,
        decimal_places=2,
        default=None,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(2000)])

    def __str__(self):
        return f'[{self.datetime:%Y-%m-%d %H:%M}] (location: {self.location}) {self.value} mmHg'

    class Meta:
        ordering = ['-datetime', 'location']
        verbose_name = _('Pressure Measurement')
        verbose_name_plural = _('Pressure')

    class Admin(admin.ModelAdmin):
        change_list_template = 'admin/change_list_filter_sidebar.html'
        list_display = ['datetime', 'location', 'value']
        list_filter = ['location']
        search_fields = ['^datetime', 'value']
