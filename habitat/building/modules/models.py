from django.contrib import admin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Module(models.Model):
    STATUSES_CHOICES = [
        ('nominal', _('Working Nominal')),
        ('locked', _('Locked')),
        ('disabled', _('Disabled')),
        ('under-construction', _('Under Construction')),
        ('destructed', _('Destructed'))]

    HAZARD_CHOICES = [
        ('none', _('None')),
        ('warning', _('Warning')),
        ('hazardous', _('Hazardous')),
        ('toxic', _('Toxic')),
        ('depress', _('Hazardous')),
        ('fire', _('Fire')),
        ('disabled', _('Disabled'))]

    PLAN_CHOICES = [
        ('ellipsis', _('Ellipsis')),
        ('rectangle', _('Rectangle')),
        ('polygon', _('Polygon')),
        ('other', _('Other'))]

    name = models.CharField(verbose_name=_('Name'), max_length=255, db_index=True, default=None)
    status = models.CharField(verbose_name=_('Status'), choices=STATUSES_CHOICES, max_length=30, db_index=True, default='nominal')
    hazard = models.CharField(verbose_name=_('Hazard'), choices=HAZARD_CHOICES, max_length=30, db_index=True, default=None)
    blueprint = models.ImageField(verbose_name=_('Blueprint'), upload_to='modules/', null=True, blank=True, default=None)

    width = models.DecimalField(verbose_name=_('Width'), help_text=_('m'), max_digits=4, decimal_places=2, validators=[MaxValueValidator(99), MinValueValidator(0)], null=True, blank=True, default=None)
    height = models.DecimalField(verbose_name=_('Height'), help_text=_('m'), max_digits=4, decimal_places=2, validators=[MaxValueValidator(99), MinValueValidator(0)], null=True, blank=True, default=None)
    length = models.DecimalField(verbose_name=_('Length'), help_text=_('m'), max_digits=4, decimal_places=2, validators=[MaxValueValidator(99), MinValueValidator(0)], null=True, blank=True, default=None)
    plan = models.CharField(verbose_name=_('Plan'), choices=PLAN_CHOICES, max_length=30, default=None)
    capacity = models.PositiveIntegerField(verbose_name=_('Capacity'), help_text=_('Max crew members working inside.'), null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        verbose_name = _('Module')
        verbose_name_plural = _('Modules')

    class Admin(admin.ModelAdmin):
        change_list_template = 'admin/change_list_filter_sidebar.html'
        list_display = ['name', 'status', 'hazard', 'width', 'height', 'length', 'plan', 'capacity']
        list_filter = ['status', 'hazard']
        search_fields = ['name']
