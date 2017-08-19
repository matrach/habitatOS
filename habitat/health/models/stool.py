from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime
from habitat._common.models import ReporterAstronaut


class Stool(HabitatModel, MissionDateTime, ReporterAstronaut):
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

    volume = models.PositiveIntegerField(verbose_name=_('Volume'), help_text=_('ml'), null=True, blank=True, default=None, validators=[MinValueValidator(0), MaxValueValidator(1700)])
    color = models.CharField(verbose_name=_('Color'), choices=COLOR_CHOICES, max_length=30, default=COLOR_BROWN)
    type = models.CharField(verbose_name=_('Type'), choices=TYPE_CHOICES, max_length=30, default=TYPE_SMOOTH)
    abnormalities = models.CharField(verbose_name=_('Abnormalities'), choices=ABNORMALITIES_CHOICES, max_length=30, null=True, blank=True)

    def __str__(self):
        return f'[{self.date} {self.time}] <{self.reporter}> {self.volume}ml, {self.color}, {self.type}, {self.abnormalities}'

    class Meta:
        verbose_name = _('Stool')
        verbose_name_plural = _('Stool')
