from django.contrib import admin
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


class ProductCategory(models.Model):
    parent = models.ForeignKey(verbose_name=_('Parent'), to='food.ProductCategory', db_index=True, null=True, blank=True, default=None)
    name = models.CharField(verbose_name=_('Name'), max_length=255, db_index=True, default=None)
    slug = models.SlugField(verbose_name=_('Slug'), editable=False, db_index=True, default=None)

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.name}'
        else:
            return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.__str__())
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Product Category')
        verbose_name_plural = _('Product Categories')

    class Admin(admin.ModelAdmin):
        ordering = ['slug', 'name']
        list_display = ['parent', 'name']
        list_display_links = ['name']
        search_fields = ['^name']
        list_filter = ['parent']
