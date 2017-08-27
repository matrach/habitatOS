from django.contrib import admin
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.forms import CheckboxSelectMultiple
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


def upload_path(instance, filename):
    extension = filename.split('.')[-1]
    return f'products/{instance.category}/{instance.slug}.{extension}'


class ProductUsageUnits(models.Model):
    unit = models.ForeignKey(verbose_name=_('Unit'), to='food.Unit', limit_choices_to={'type': 'usage'}, default=None)
    value = models.PositiveSmallIntegerField(verbose_name=_('Value'), default=None)

    def __str__(self):
        return f'{self.value} {self.unit}'


class ProductShoppingUnits(models.Model):
    unit = models.ForeignKey(verbose_name=_('Unit'), to='food.Unit', limit_choices_to={'type': 'shopping'}, default=None)
    value = models.PositiveSmallIntegerField(verbose_name=_('Value'), default=None)

    def __str__(self):
        return f'{self.value} {self.unit}'


class Product(models.Model):
    TYPE_CHOICES = [
        ('custom', _('Custom Made')),
        ('brand', _('Brand Product')),
        ('gourmet', _('Gourmet Food')),
        ('restaurant', _('Restaurant'))]

    FORM_CHOICES = [
        ('solid', _('Solid')),
        ('liquid', _('Liquid'))]

    CATEGORY_CHOICES = [
        ('other', _('Other')),
        ('fruits', _('Fruits')),
        ('vegetables', _('Vegetables')),
        ('meat', _('Meat'))]

    name = models.CharField(verbose_name=_('Name'), max_length=255, db_index=True, default=None)
    slug = models.SlugField(verbose_name=_('Slug'), editable=False, db_index=True, default=None)
    image = models.ImageField(verbose_name=_('Image'), upload_to=upload_path, null=True, blank=True, default=None)
    type = models.CharField(verbose_name=_('Type'), choices=TYPE_CHOICES, max_length=30, db_index=True, default=None)
    category = models.CharField(verbose_name=_('Category'), choices=CATEGORY_CHOICES, max_length=30, db_index=True, default=None)
    tags = models.ManyToManyField(verbose_name=_('Tags'), to='food.Tag', limit_choices_to={'type': 'product'}, blank=True, default=None)

    modification_date = models.DateTimeField(verbose_name=_('Modification Date'), auto_now=True)
    modification_author = models.ForeignKey(verbose_name=_('Modification Author'), to='auth.User', default=None)

    measurements_physical_form = models.CharField(verbose_name=_('Phisical Form'), choices=FORM_CHOICES, max_length=20, db_index=True, blank=True, null=True, default=None)
    measurements_usage_unit = models.ForeignKey(verbose_name=_('Usage Unit'), to='food.Unit', related_name='usage_unit', blank=True, null=True, default=None)
    measurements_shopping_unit = models.ForeignKey(verbose_name=_('Shopping Unit'), to='food.Unit', related_name='shopping_unit', blank=True, null=True, default=None)
    measurements_volume = models.DecimalField(verbose_name=_('Volume'), help_text=_('ml'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    measurements_weight = models.DecimalField(verbose_name=_('Net Weight'), help_text=_('g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)

    calories = models.PositiveSmallIntegerField(verbose_name=_('Calories'), help_text=_('kcal'), blank=True, null=True, default=None)

    roughage = models.DecimalField(verbose_name=_('Roughage'), help_text=_('g/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)

    cooking_waste = models.DecimalField(verbose_name=_('Cooking Waste'), decimal_places=2, max_digits=3, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], blank=True, null=True, default=None)
    cooking_factor = models.IntegerField(verbose_name=_('Cooking Factor'), blank=True, null=True, default=None)
    cooking_product = models.ForeignKey(verbose_name=_('From Product'), to='food.Product', blank=True, null=True, default=None)

    proteins = models.DecimalField(verbose_name=_('Proteins'), help_text=_('g/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    proteins_animal = models.DecimalField(verbose_name=_('Animal Proteins'), help_text=_('g/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    proteins_plant = models.DecimalField(verbose_name=_('Plant Proteins'), help_text=_('g/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)

    fats = models.DecimalField(verbose_name=_('Fats'), help_text=_('g/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    fats_saturated = models.DecimalField(verbose_name=_('Saturated Fats'), help_text=_('g/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    fats_monounsaturated = models.DecimalField(verbose_name=_('Monounsaturated Fats'), help_text=_('g/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    fats_polyunsaturated = models.DecimalField(verbose_name=_('Polyunsaturated Fats'), help_text=_('g/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    cholesterol = models.DecimalField(verbose_name=_('Cholesterol'), help_text=_('g/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)

    carbohydrates = models.DecimalField(verbose_name=_('Carbohydrates'), help_text=_('g/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    carbohydrates_sugars = models.DecimalField(verbose_name=_('Sugars'), help_text=_('g/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)

    vitamins_folic_acid = models.DecimalField(verbose_name=_('Folic Acid'), help_text=_('µg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    vitamins_a = models.DecimalField(verbose_name=_('Vitamin A'), help_text=_('µg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    vitamins_b1 = models.DecimalField(verbose_name=_('Vitamin B1'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    vitamins_b2 = models.DecimalField(verbose_name=_('Vitamin B2'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    vitamins_b6 = models.DecimalField(verbose_name=_('Vitamin B6'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    vitamins_b12 = models.DecimalField(verbose_name=_('Vitamin B12'), help_text=_('µg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    vitamins_c = models.DecimalField(verbose_name=_('Vitamin C'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    vitamins_d = models.DecimalField(verbose_name=_('Vitamin D'), help_text=_('µg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    vitamins_e = models.DecimalField(verbose_name=_('Vitamin E'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    vitamins_pp = models.DecimalField(verbose_name=_('Vitamin PP'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)

    minerals_zinc = models.DecimalField(verbose_name=_('Zinc'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    minerals_phosphorus = models.DecimalField(verbose_name=_('Phosphorus'), help_text=_('mg/100g'),  decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    minerals_iodine = models.DecimalField(verbose_name=_('Iodine'), help_text=_('µg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    minerals_magnesium = models.DecimalField(verbose_name=_('Magnesium'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    minerals_copper = models.DecimalField(verbose_name=_('Copper'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    minerals_potasium = models.DecimalField(verbose_name=_('Potasium'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    minerals_selenium = models.DecimalField(verbose_name=_('Selenium'), help_text=_('µg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    minerals_sodium = models.DecimalField(verbose_name=_('Sodium'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    minerals_calcium = models.DecimalField(verbose_name=_('Calcium'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
    minerals_iron = models.DecimalField(verbose_name=_('Iron'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)

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
        ordering = ['-name']
        list_display = ['name', 'type', 'category', 'modification_author', 'modification_date', 'display_tags']
        list_filter = ['type', 'category', 'tags', 'modification_author', 'modification_date']
        search_fields = ['name']
        fieldsets = [
            (_('General'), {'fields': ['name', 'type', 'category', 'tags', 'image']}),
            (_('Measurements'), {'fields': ['measurements_physical_form', 'measurements_usage_unit', 'measurements_shopping_unit', 'measurements_volume', 'measurements_weight']}),
            (_('Cooking'), {'fields': ['cooking_waste', 'cooking_factor', 'cooking_product']}),
            (_('Nutrition'), {'fields': ['calories', 'roughage']}),
            (_('Proteins'), {'fields': ['proteins', 'proteins_animal', 'proteins_plant']}),
            (_('Fats'), {'fields': ['fats', 'fats_saturated', 'fats_monounsaturated', 'fats_polyunsaturated', 'cholesterol']}),
            (_('Carbohydrates'), {'fields': ['carbohydrates', 'carbohydrates_sugars']}),
            (_('Vitamins'), {'fields': ['vitamins_folic_acid', 'vitamins_a', 'vitamins_b1', 'vitamins_b2', 'vitamins_b6', 'vitamins_b12', 'vitamins_c', 'vitamins_d', 'vitamins_e', 'vitamins_pp']}),
            (_('Minerals'), {'fields': ['minerals_zinc', 'minerals_phosphorus', 'minerals_iodine', 'minerals_magnesium', 'minerals_copper', 'minerals_potasium', 'minerals_selenium', 'minerals_calcium', 'minerals_iron']}),
        ]

        def display_tags(self, obj):
            return ", ".join([tag.name for tag in obj.tags.all()])

        display_tags.short_description = _('Tags')

        def save_model(self, request, obj, form, change):
            obj.modification_author = User.objects.get(id=request.user.id)
            super().save_model(request, obj, form, change)
