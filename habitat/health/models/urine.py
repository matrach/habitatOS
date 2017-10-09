from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime
from habitat._common.models import ReporterAstronaut


class Urine(HabitatModel, MissionDateTime, ReporterAstronaut):
    COLOR_COLORLESS = 'colorless'
    COLOR_YELLOW_LIGHT = 'yellow-light'
    COLOR_YELLOW = 'yellow'
    COLOR_YELLOW_AMBER = 'yellow-amber'
    COLOR_YELLOW_BROWN = 'yellow-brown'
    COLOR_AMBER = 'amber'
    COLOR_ORANGE = 'orange'
    COLOR_RED = 'red'
    COLOR_GREENISH_BROWN = 'greenish-brown'

    COLOR_CHOICES = [
        (COLOR_COLORLESS, _('Colorless')),
        (COLOR_YELLOW_LIGHT, _('Light Yellow')),
        (COLOR_YELLOW, _('Yellow')),
        (COLOR_YELLOW_AMBER, _('Yellow Amber')),
        (COLOR_YELLOW_BROWN, _('Yellow Brown')),
        (COLOR_AMBER, _('Amber')),
        (COLOR_ORANGE, _('Orange')),
        (COLOR_RED, _('Red')),
        (COLOR_GREENISH_BROWN, _('Greenish Brown')),
    ]

    TURBIDITY_CLEAR = 'clear'
    TURBIDITY_SLIGHTLY = 'slightly'
    TURBIDITY_CLOUDY = 'cloudy'
    TURBIDITY_TURBID = 'turbid'

    TURBIDITY_CHOICES = [
        (TURBIDITY_CLEAR, _('Clear')),
        (TURBIDITY_SLIGHTLY, _('Slightly')),
        (TURBIDITY_CLOUDY, _('Cloudy')),
        (TURBIDITY_TURBID, _('Turbid')),
    ]

    volume = models.PositiveIntegerField(verbose_name=_('Volume'), help_text=_('ml'), default=None, validators=[MinValueValidator(0), MaxValueValidator(5000)])
    color = models.CharField(verbose_name=_('Color'), max_length=30, choices=COLOR_CHOICES, default=COLOR_YELLOW)
    turbidity = models.CharField(verbose_name=_('Turbidity'), max_length=30, choices=TURBIDITY_CHOICES, default=TURBIDITY_CLEAR)
    ph = models.DecimalField(verbose_name=_('pH'), max_digits=3, decimal_places=1, null=True, blank=True, default=None, validators=[MinValueValidator(0), MaxValueValidator(12)])

    def __str__(self):
        return f'[{self.date} {self.time}] <{self.reporter}> {self.volume}ml, {self.color}, {self.turbidity}, {self.ph}'

    class Meta:
        verbose_name = _('Urine')
        verbose_name_plural = _('Urine')
