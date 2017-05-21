from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin


class Plant(models.Model):
    latin_name = models.CharField(
        verbose_name=_('Latin Name'),
        max_length=255,
        default=None)

    spicies = models.CharField(
        verbose_name=_('Species'),
        max_length=255,
        default=None)

    image = models.ImageField(
        verbose_name=_('Image'),
        default=None,
        blank=True,
        null=True)

    wikipedia_url = models.URLField(
        verbose_name=_('Wikipedia URL'),
        default=None,
        blank=True,
        null=True)

    def __str__(self):
        return f'{self.spicies} ({self.latin_name})'

    class Meta:
        ordering = ['-latin_name']

    class Admin(admin.ModelAdmin):
        list_display = ['latin_name', 'spicies', 'wikipedia_url']
        search_fields = ['latin_name', 'spicies']
