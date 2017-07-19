from django.contrib import admin
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.forms import CheckboxSelectMultiple
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


class DayPlan(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=255, db_index=True, default=None)
    slug = models.SlugField(verbose_name=_('Slug'), editable=False, default=None)
    diet = models.ManyToManyField(verbose_name=_('Diet'), to='food.Diet', blank=True, default=None)
    calories = models.PositiveIntegerField(verbose_name=_('Calories'), validators=[MaxValueValidator(5000), MinValueValidator(0)], blank=True, default=None)

    breakfast = models.ForeignKey(verbose_name=_('Breakfast'), to='food.Meal', related_name='breakfast', blank=True, default=None)
    brunch = models.ForeignKey(verbose_name=_('Brunch'), to='food.Meal', related_name='brunch', blank=True, default=None)
    lunch = models.ForeignKey(verbose_name=_('Lunch'), to='food.Meal', related_name='lunch', blank=True, default=None)
    tea = models.ForeignKey(verbose_name=_('Tea'), to='food.Meal', related_name='tea', blank=True, default=None)
    supper = models.ForeignKey(verbose_name=_('Supper'), to='food.Meal', related_name='supper', blank=True, default=None)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-name']
        verbose_name = _('Day Plan')
        verbose_name_plural = _('Day Plans')

    class Admin(admin.ModelAdmin):
        formfield_overrides = {models.ManyToManyField: {'widget': CheckboxSelectMultiple}}
        list_display = ['name', 'calories', 'display_diet']
        ordering = ['-name']
        search_fields = ['^name']

        def display_diet(self, obj):
            return ", ".join([diet.name for diet in obj.diet.all()])

        display_diet.short_description = _('Diet')
