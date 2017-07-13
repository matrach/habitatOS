from django.contrib import admin
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.forms import CheckboxSelectMultiple
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


def upload_path(instance, filename):
    extension = filename.split('.')[-1]
    return f'products/{instance.category}/{instance.slug}.{extension}'


class Meal(models.Model):
    KINDS = [
        ('', _('')),
    ]

    name = models.CharField(verbose_name=_('Name'), max_length=255, db_index=True, default=None)
    slug = models.SlugField(verbose_name=_('Slug'), editable=False, db_index=True, default=None)
    image = models.ImageField(verbose_name=_('Image'), upload_to=upload_path, null=True, blank=True, default=None)
    kind = models.CharField(verbose_name=_('Kind'), choices=KINDS, max_length=30, db_index=True, default=None)
    category = models.CharField(verbose_name=_('Category'), choices=CATEGORIES, max_length=30, db_index=True, default=None)
    tags = models.ManyToManyField(verbose_name=_('Tags'), to='food.Tag', default=None)


    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-name']
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    class Admin(admin.ModelAdmin):
        change_list_template = 'admin/change_list_filter_sidebar.html'
        formfield_overrides = {models.ManyToManyField: {'widget': CheckboxSelectMultiple}}
        list_display = ['name', 'kind', 'category', 'display_tags']
        ordering = ['-name']
        search_fields = ['name']
        list_filter = ['kind', 'category', 'tags']
        fieldsets = [
            (_('General'), {'fields': ['name', 'kind', 'category', 'image', 'tags']}),
            (_('Measurements'),
                {'fields': ['measurements_physical_form', 'measurements_usage_unit', 'measurements_shopping_unit',
                           'measurements_volume', 'measurements_weight']}),
            (_('Cooking'), {'fields': ['cooking_waste', 'cooking_factor', 'cooking_product']}),
            (_('Nutrition'), {'fields': ['calories', 'roughage']}),
            (_('Proteins'), {'fields': ['proteins', 'proteins_animal', 'proteins_plant']}),
            (_('Fats'),
             {'fields': ['fats', 'fats_saturated', 'fats_monounsaturated', 'fats_polyunsaturated', 'cholesterol']}),
            (_('Carbohydrates'), {'fields': ['carbohydrates', 'carbohydrates_sugars']}),
            (_('Vitamins'), {
                'fields': ['vitamins_folic_acid', 'vitamins_a', 'vitamins_b1', 'vitamins_b2', 'vitamins_b6', 'vitamins_b12',
                           'vitamins_c', 'vitamins_d', 'vitamins_e', 'vitamins_pp']}),
            (_('Minerals'), {'fields': ['minerals_zinc', 'minerals_phosphorus', 'minerals_iodine', 'minerals_magnesium',
                                        'minerals_copper', 'minerals_potasium', 'minerals_selenium', 'minerals_calcium',
                                        'minerals_iron']}),
        ]

        def display_tags(self, obj):
            return ", ".join([tag.name for tag in obj.tags.all()])

        display_tags.short_description = _('Tags')
