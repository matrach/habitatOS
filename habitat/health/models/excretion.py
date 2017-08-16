from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now


class Urine(models.Model):
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
        (COLOR_YELLOW, _('yellow')),
        (COLOR_YELLOW_AMBER, _('yellow-amber')),
        (COLOR_YELLOW_BROWN, _('yellow-brown')),
        (COLOR_AMBER, _('amber')),
        (COLOR_ORANGE, _('orange')),
        (COLOR_RED, _('red')),
        (COLOR_GREENISH_BROWN, _('greenish-brown')),
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

    astronaut = models.ForeignKey(verbose_name=_('Astronaut'), to='auth.User', limit_choices_to={'groups__name': 'Astronauts'})
    datetime = models.DateTimeField(verbose_name=_('Datetime'), default=now)

    volume = models.PositiveIntegerField(verbose_name=_('Volume'), help_text=_('ml'), default=None, validators=[MinValueValidator(0), MaxValueValidator(1700)])
    color = models.CharField(verbose_name=_('Color'), max_length=30, choices=COLOR_CHOICES, default=COLOR_YELLOW)
    turbidity = models.CharField(verbose_name=_('Turbidity'), max_length=30, choices=TURBIDITY_CHOICES, default=TURBIDITY_CLEAR)
    ph = models.DecimalField(verbose_name=_('pH'), max_digits=3, decimal_places=1, null=True, blank=True, default=None, validators=[MinValueValidator(0), MaxValueValidator(12)])

    def __str__(self):
        return f'[{self.datetime}] <{self.astronaut}> {self.volume}ml, {self.color}, {self.turbidity}, {self.ph}'

    class Meta:
        ordering = ['-datetime']
        verbose_name = _('Urine')
        verbose_name_plural = _('Urine Measurements')


class Stool(models.Model):
    TYPE_HARD_LUMPS = 'hard-lumps'
    TYPE_LUMPY = 'lumpy'
    TYPE_CRACKS = 'cracks'
    TYPE_SMOOTH = 'smooth'
    TYPE_BLOBS = 'blobs'
    TYPE_FLUFFY = 'fluffy'
    TYPE_LIQUID = 'liquid'

    TYPE_CHOICES = [
        (TYPE_HARD_LUMPS, _('Separate hard lumps, like nuts (hard to pass)')),
        (TYPE_LUMPY, _('Sausage-shaped but lumpy')),
        (TYPE_CRACKS, _('Like a sausage but with cracks on the surface')),
        (TYPE_SMOOTH, _('Like a sausage or snake, smooth and soft')),
        (TYPE_BLOBS, _('Soft blobs with clear-cut edges')),
        (TYPE_FLUFFY, _('Fluffy pieces with ragged edges, a mushy stool')),
        (TYPE_LIQUID, _('Watery, no solid pieces. Entirely Liquid')),
    ]

    COLOR_BROWN = 'brown'
    COLOR_YELLOW = 'yellow'
    COLOR_GRAY = 'gray'
    COLOR_PALE = 'pale'
    COLOR_BLACK = 'black'
    COLOR_RED = 'red'
    COLOR_BLUE = 'blue'
    COLOR_SILVER = 'silver'
    COLOR_GREEN = 'green'
    COLOR_VIOLET = 'violet'
    COLOR_PURPLE = 'purple'

    COLOR_CHOICES = [
        (COLOR_BROWN, _('Brown')),
        (COLOR_YELLOW, _('Yellow')),
        (COLOR_GRAY, _('Gray')),
        (COLOR_PALE, _('Pale')),
        (COLOR_BLACK, _('Black')),
        (COLOR_RED, _('Red')),
        (COLOR_BLUE, _('Blue')),
        (COLOR_SILVER, _('Silver')),
        (COLOR_GREEN, _('Green')),
        (COLOR_VIOLET, _('Violet')),
        (COLOR_PURPLE, _('Purple')),
    ]

    ABNORMALITIES_UNDIGESTED_FOOD = 'undigested-food'
    ABNORMALITIES_DIARRHEA = 'diarrhea'
    ABNORMALITIES_CONSTIPATION = 'constipation'
    ABNORMALITIES_OTHERS = 'others'

    ABNORMALITIES_CHOICES = [
        (ABNORMALITIES_UNDIGESTED_FOOD, _('Undigested food remnants')),
        (ABNORMALITIES_DIARRHEA, _('Diarrhea')),
        (ABNORMALITIES_CONSTIPATION, _('Constipation')),
        (ABNORMALITIES_OTHERS, _('Others')),
    ]

    astronaut = models.ForeignKey(verbose_name=_('Astronaut'), to='auth.User', limit_choices_to={'groups__name': 'Astronauts'})
    datetime = models.DateTimeField(verbose_name=_('Datetime'), default=now)

    volume = models.PositiveIntegerField(verbose_name=_('Volume'), help_text=_('ml'), null=True, blank=True, default=None, validators=[MinValueValidator(0), MaxValueValidator(1700)])
    color = models.CharField(verbose_name=_('Color'), choices=COLOR_CHOICES, max_length=30, null=True, blank=True, default=COLOR_BROWN)
    type = models.CharField(verbose_name=_('Type'), choices=TYPE_CHOICES, max_length=30, null=True, blank=True, default=TYPE_SMOOTH)
    abnormalities = models.CharField(verbose_name=_('Abnormalities'), choices=ABNORMALITIES_CHOICES, max_length=30, null=True, blank=True)

    def __str__(self):
        return f'[{self.datetime}] <{self.astronaut}> {self.volume}ml, {self.color}, {self.consistency}'

    class Meta:
        ordering = ['-datetime']
        verbose_name = _('Stool')
        verbose_name_plural = _('Stool Measurements')
