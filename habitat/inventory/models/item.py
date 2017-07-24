from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Item(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        default=None,
        max_length=255)

    code = models.CharField(
        verbose_name=_('Code'),
        default=None,
        max_length=7)

    quantity = models.PositiveSmallIntegerField(
        verbose_name=_('Quantity'),
        default=1)

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
