from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator


class CarbonDioxide(models.Model):

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
        verbose_name=_('Concentration'),
        help_text=_('%'),
        max_digits=5,
        decimal_places=3,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)])

    def __str__(self):
        return f'[{self.datetime}] (location: {self.location}) {self.value}%'

    class Meta:
        ordering = ['-datetime', 'location']
        verbose_name = _('Carbon Dioxide Concentration Measurement')
        verbose_name_plural = _('Carbon Dioxide')

    class Admin(admin.ModelAdmin):
        change_list_template = 'admin/change_list_filter_sidebar.html'
        list_display = ['datetime', 'location', 'value']
        list_filter = ['location']
        search_fields = ['^datetime', 'value']
