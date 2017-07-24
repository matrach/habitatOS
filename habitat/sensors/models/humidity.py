from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator


class Humidity(models.Model):

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
        verbose_name=_('Humidity'),
        help_text=_('%'),
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)])

    def __str__(self):
        return f'[{self.datetime}] (location: {self.location}) {self.value}%'

    class Meta:
        ordering = ['-datetime', 'location']
        verbose_name = _('Humitdity Measurement')
        verbose_name_plural = _('Humidity')

    class Admin(admin.ModelAdmin):
        change_list_template = 'admin/change_list_filter_sidebar.html'
        list_display = ['datetime', 'location', 'value']
        list_filter = ['location']
        search_fields = ['^datetime', 'value']
