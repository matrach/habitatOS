from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.contrib import admin


class Temperature(models.Model):
    astronaut = models.ForeignKey(
        to='auth.User',
        limit_choices_to={'groups__name': 'Astronauts'})

    datetime = models.DateTimeField(
        verbose_name=_('Datetime'),
        default=now)

    temperature = models.DecimalField(
        verbose_name=_('Temperature'),
        help_text=_('Celsius'),
        max_digits=3,
        decimal_places=1,
        validators=[
            MaxValueValidator(42),
            MinValueValidator(30)])

    def __str__(self):
        return f'[{self.datetime}] {self.astronaut} Temp: {self.temperature}'

    class Meta:
        ordering = ['-datetime']

    class Admin(admin.ModelAdmin):
        list_display = ['datetime', 'astronaut', 'temperature']