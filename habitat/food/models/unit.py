from django.contrib import admin
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


class Unit(models.Model):
    TYPE_CHOICES = [
        ('shopping', _('Shopping')),
        ('usage', _('Usage')),
    ]

    name = models.CharField(verbose_name=_('Name'), max_length=255, db_index=True, default=None)
    slug = models.SlugField(verbose_name=_('Slug'), editable=False, default=None)
    type = models.CharField(verbose_name=_('Type'), max_length=30, choices=TYPE_CHOICES, default='usage')

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Unit')
        verbose_name_plural = _('Units')

    class Admin(admin.ModelAdmin):
        list_display = ['name', 'type']
        ordering = ['-name']
        search_fields = ['^name']
        list_editable = ['type']
