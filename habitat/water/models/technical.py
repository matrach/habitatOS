from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.contrib import admin


class TechnicalWater(models.Model):
    astronaut = models.ForeignKey(verbose_name=_('Astronaut'), to='auth.User', limit_choices_to={'groups__name': 'Astronauts'})
    datetime = models.DateTimeField(verbose_name=_('Datetime'), default=now)
    volume = models.DecimalField(verbose_name=_('Volume'), help_text=_('liters'), max_digits=3, decimal_places=2, default=None, validators=[MinValueValidator(0), MaxValueValidator(9.99)])
    usage_description = models.TextField(verbose_name=_('Usage Description'), null=True, blank=True, default=None)

    def __str__(self):
        return f'[{self.datetime:%Y-%m-%d %H:%M}] {self.astronaut} {self.volume}l'

    class Meta:
        ordering = ['-datetime']
        verbose_name = _('Technical Water Measurement')
        verbose_name_plural = _('Technical Water Usage')

    class Admin(admin.ModelAdmin):
        list_display = ['datetime', 'astronaut', 'volume', 'usage_description']
        date_hierarchy = 'datetime'
