from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel


class Module(HabitatModel):
    STATUS_NOMINAL = 'nominal'
    STATUS_LOCKED = 'locked'
    STATUS_DISABLED = 'disabled'
    STATUS_UNDER_CONSTRUCTION = 'under-construction'
    STATUS_DESTRUCTED = 'destructed'

    STATUSES_CHOICES = [
        (STATUS_NOMINAL, _('Working Nominal')),
        (STATUS_LOCKED, _('Locked')),
        (STATUS_DISABLED, _('Disabled')),
        (STATUS_UNDER_CONSTRUCTION, _('Under Construction')),
        (STATUS_DESTRUCTED, _('Destructed')),
    ]

    HAZARD_NONE = 'none'
    HAZARD_WARNING = 'warning'
    HAZARD_HAZARDOUS = 'hazardous'
    HAZARD_TOXIC = 'toxic'
    HAZARD_DEPRESS = 'depress'
    HAZARD_FIRE = 'fire'
    HAZARD_DISABLED = 'disabled'

    HAZARD_CHOICES = [
        (HAZARD_NONE, _('None')),
        (HAZARD_WARNING, _('Warning')),
        (HAZARD_HAZARDOUS, _('Hazardous')),
        (HAZARD_TOXIC, _('Toxic')),
        (HAZARD_DEPRESS, _('Hazardous')),
        (HAZARD_FIRE, _('Fire')),
        (HAZARD_DISABLED, _('Disabled')),
    ]

    PLAN_ELLIPSIS = 'ellipsis'
    PLAN_RECTANGLE = 'rectangle'
    PLAN_POLYGON = 'polygon'
    PLAN_OTHER = 'other'

    PLAN_CHOICES = [
        (PLAN_ELLIPSIS, _('Ellipsis')),
        (PLAN_RECTANGLE, _('Rectangle')),
        (PLAN_POLYGON, _('Polygon')),
        (PLAN_OTHER, _('Other')),
    ]

    name = models.CharField(verbose_name=_('Name'), max_length=255, db_index=True, default=None)
    status = models.CharField(verbose_name=_('Status'), choices=STATUSES_CHOICES, max_length=30, db_index=True, default=STATUS_NOMINAL)
    hazard = models.CharField(verbose_name=_('Hazard'), choices=HAZARD_CHOICES, max_length=30, db_index=True, default=HAZARD_NONE)
    blueprint = models.ImageField(verbose_name=_('Blueprint'), upload_to='building/', null=True, blank=True, default=None)

    width = models.DecimalField(verbose_name=_('Width'), help_text=_('m'), max_digits=4, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(99)], null=True, blank=True, default=None)
    height = models.DecimalField(verbose_name=_('Height'), help_text=_('m'), max_digits=4, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(99)], null=True, blank=True, default=None)
    length = models.DecimalField(verbose_name=_('Length'), help_text=_('m'), max_digits=4, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(99)], null=True, blank=True, default=None)
    plan = models.CharField(verbose_name=_('Plan'), choices=PLAN_CHOICES, max_length=30, default=PLAN_RECTANGLE)
    capacity = models.PositiveIntegerField(verbose_name=_('Capacity'), help_text=_('Max crew members working inside.'), null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Module')
        verbose_name_plural = _('Modules')
