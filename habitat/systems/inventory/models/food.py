from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Food(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    code = models.CharField(verbose_name=_('Code'), max_length=7)
    best_before = models.DateField(verbose_name=_('Best before'))
    calories = models.PositiveSmallIntegerField(verbose_name=_('Calories'), help_text=_('kcal'))

    volume = models.DecimalField(
        verbose_name=_('Volume'),
        help_text=_('ml'),
        decimal_places=2,
        max_digits=5,
        blank=True,
        null=True)

    weight = models.DecimalField(
        verbose_name=_('Net Weight'),
        help_text=_('g'),
        decimal_places=2,
        max_digits=5,
        blank=True,
        null=True)

    proteins = models.DecimalField(
        verbose_name=_('Proteins'),
        help_text=_('g'),
        decimal_places=2,
        max_digits=5,
        blank=True,
        null=True)

    carbohydrates = models.DecimalField(
        verbose_name=_('Carbohydrates'),
        help_text=_('g'),
        decimal_places=2,
        max_digits=5,
        blank=True,
        null=True)

    fats = models.DecimalField(
        verbose_name=_('Fats'),
        help_text=_('g'),
        decimal_places=2,
        max_digits=5,
        blank=True,
        null=True)

    salt = models.DecimalField(
        verbose_name=_('Salts'),
        help_text=_('g'),
        decimal_places=2,
        max_digits=5,
        blank=True,
        null=True)

    def __str__(self):
        return f'[{self.code}] {self.name} (best before: {self.best_before:%Y-%m-%d}'

    class Admin(admin.ModelAdmin):
        list_display = ['code', 'name', 'best_before', 'calories']
        ordering = ['-best_before']
        search_fields = ['^code', 'name']
