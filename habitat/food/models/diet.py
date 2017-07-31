from django.contrib import admin
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


class Diet(models.Model):
    TYPE_CHOICES = [
        ('basic', _('Basic')),
        ('healthy', _('Healthy')),
        ('sport', _('Sport'))]

    name = models.CharField(verbose_name=_('Name'), max_length=255, db_index=True, default=None)
    type = models.CharField(verbose_name=_('Type'), choices=TYPE_CHOICES, max_length=30, db_index=True, null=True, blank=True, default=None)
    slug = models.SlugField(verbose_name=_('Slug'), editable=False, default=None)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-name']
        verbose_name = _('Diet')
        verbose_name_plural = _('Diets')

    class Admin(admin.ModelAdmin):
        change_list_template = 'admin/change_list_filter_sidebar.html'
        list_display = ['name', 'type']
        ordering = ['-name']
        search_fields = ['^name']
