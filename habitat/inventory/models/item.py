from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Item(models.Model):
    TYPE_SOLID = 'solid'
    TYPE_LIQUID = 'liquid'

    TYPE_CHOICES = [
        (TYPE_SOLID, _('Solid')),
        (TYPE_LIQUID, _('Liquid')),
    ]

    name = models.CharField(
        verbose_name=_('Name'),
        default=None,
        max_length=255)

    manufacturer = models.CharField(
        verbose_name=_('Name'),
        default=None,
        max_length=255)

    type = models.CharField(
        verbose_name=_('Type'),
        max_length=30,
        choices=TYPE_CHOICES,
        default=TYPE_SOLID)

    code = models.CharField(
        verbose_name=_('Code'),
        max_length=7,
        null=True,
        blank=True,
        default=None)

    location = models.ForeignKey(
        verbose_name=_('Location'),
        to='building.Storage')

    volume = models.PositiveIntegerField(
        verbose_name=_('Volume'),
        help_text=_('liters'),
        null=True,
        blank=True,
        default=None)

    height = models.PositiveIntegerField(
        verbose_name=_('Height'),
        help_text=_('meters'),
        null=True,
        blank=True,
        default=None)

    width = models.PositiveIntegerField(
        verbose_name=_('Width'),
        help_text=_('meters'),
        null=True,
        blank=True,
        default=None)

    length = models.PositiveIntegerField(
        verbose_name=_('Length'),
        help_text=_('meters'),
        null=True,
        blank=True,
        default=None)

    quantity = models.PositiveSmallIntegerField(
        verbose_name=_('Quantity'),
        null=True,
        blank=True,
        default=1)

    remarks = models.TextField(
        verbose_name=_('Remarks'),
        null=True,
        blank=True,
        default=None)

    def __str__(self):
        return f'[{self.code}] {self.name} Quantity: {self.quantity}'

    class Meta:
        ordering = ['code']
        verbose_name = _('Item')
        verbose_name_plural = _('Item Database')

    class Admin(admin.ModelAdmin):
        list_display = ['code', 'name', 'quantity']
        ordering = ['code']
        search_fields = ['^code', 'name']
