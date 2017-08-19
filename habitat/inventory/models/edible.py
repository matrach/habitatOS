from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel


class Edible(HabitatModel):
    code = models.CharField(verbose_name=_('Code'), default=None, max_length=7)
    product = models.ForeignKey(verbose_name=_('Product'), to='food.Product')
    quantity = models.PositiveSmallIntegerField(verbose_name=_('Quantity'), default=1)
    best_before = models.DateField(verbose_name=_('Best before'), default=None)

    def __str__(self):
        return f'[{self.code}] {self.product.name} Quantity: {self.quantity}'

    class Meta:
        ordering = ['code']
        verbose_name = _('Edible')
        verbose_name_plural = _('Edibles Database')
