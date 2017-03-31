from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class Observation(models.Model):
    experiment = models.ForeignKey(verbose_name=_('Experiment'), to='greenhouse.experiment')
    datetime = models.DateTimeField(verbose_name=_('Observation date'), default=timezone.now)
    notes = models.TextField(verbose_name=_('Notes'), blank=True, null=True)
    image = models.ImageField(verbose_name=_('Image'), blank=True, null=True)


class ObservationInline(admin.TabularInline):
    model = Observation
    extra = 1


class Experiment(models.Model):
    CULTIVATION_METHODS = [
        ('soil', _('Soil')),
        ('underwater', _('Underwater')),
        ('artificial', _('Artificial')),
        ('hydroponics', _('Hydroponics')),
        ('aeroponics', _('Aeroponics')),
        ('mixed', _('Mixed')),
        ('other', _('Other')),
    ]

    plant = models.ForeignKey(verbose_name=_('Plant'), to='greenhouse.Plant')
    cultivation_method = models.CharField(verbose_name=_('Cultivation method'), choices=CULTIVATION_METHODS, max_length=30)
    planted_date = models.DateTimeField(verbose_name=_('Date Planted'), default=timezone.now)
    image = models.ImageField(verbose_name=_('Image'), blank=True, null=True)

    class Admin(admin.ModelAdmin):
        inlines = [ObservationInline]
