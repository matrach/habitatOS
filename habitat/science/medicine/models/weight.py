from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.contrib import admin

"""
Body Fat
Lean Body Mass
Body Water
Muscle Mass
Daily Caloric Intake
Bone Mass
Visceral Fat
"""


class Weight(models.Model):
    astronaut = models.ForeignKey(
        to='auth.User',
        limit_choices_to={'groups__name': 'Astronauts'})

    datetime = models.DateTimeField(
        verbose_name=_('Datetime'),
        default=now)

    weight = models.DecimalField(
        verbose_name=_('Weight'),
        max_digits=4,
        decimal_places=1,
        validators=[
            MaxValueValidator(130),
            MinValueValidator(30)])

    BMI = models.DecimalField(
        verbose_name=_('BMI'),
        max_digits=3,
        decimal_places=1,
        blank=False,
        null=False,
        validators=[
            MaxValueValidator(40),
            MinValueValidator(10)])

    def __str__(self):
        return f'[{self.datetime}] {self.astronaut} Weight: {self.weight}, BMI: {self.BMI}'

    class Meta:
        ordering = ['-datetime']

    class Admin(admin.ModelAdmin):
        list_display = ['datetime', 'astronaut', 'weight', 'BMI']
