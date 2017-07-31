from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


def upload_path(instance, filename):
    extension = filename.split('.')[-1]
    return f'products/{instance.category}/{instance.slug}.{extension}'


class Meal(models.Model):
    TYPES = [
        ('breakfast', _('Breakfast')),
        ('brunch', _('Brunch')),
        ('lunch', _('Lunch')),
        ('tea', _('Tea')),
        ('supper', _('Supper'))]

    DIFFICULTIES = [
        ('easy', _('Easy')),
        ('medium', _('Medium')),
        ('hard', _('Hard'))]

    name = models.CharField(verbose_name=_('Name'), max_length=255, db_index=True, default=None)
    slug = models.SlugField(verbose_name=_('Slug'), editable=False, db_index=True, default=None)
    preparation_time = models.CharField(verbose_name=_('Preparation Time'), help_text=_('Example: 12h pickiling + 2h preparation + 2h cooking'), max_length=255, null=True, blank=True, default=None)
    difficulty = models.CharField(verbose_name=_('Difficulty'), choices=DIFFICULTIES, max_length=30, db_index=True, null=True, blank=True, default=None)
    type = models.CharField(verbose_name=_('Type'), choices=TYPES, max_length=30, db_index=True, null=True, blank=True, default=None)
    diet = models.ManyToManyField(verbose_name=_('Diet'), to='food.Diet', blank=True, default=None)
    tags = models.ManyToManyField(verbose_name=_('Tags'), to='food.Tag', limit_choices_to={'type': 'meal'}, blank=True, default=None)
    image = models.ImageField(verbose_name=_('Image'), upload_to=upload_path, null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-name']
        verbose_name = _('Meal')
        verbose_name_plural = _('Meals')

    class Admin(admin.ModelAdmin):
        change_list_template = 'admin/change_list_filter_sidebar.html'
        formfield_overrides = {models.ManyToManyField: {'widget': CheckboxSelectMultiple}}
        list_display = ['name', 'difficulty', 'type', 'display_diet', 'display_tags']
        ordering = ['-name']
        search_fields = ['name']
        list_filter = ['difficulty', 'type', 'diet', 'tags']

        def display_tags(self, obj):
            return ", ".join([tag.name for tag in obj.tags.all()])

        display_tags.short_description = _('Tags')

        def display_diet(self, obj):
            return ", ".join([diet.name for diet in obj.diet.all()])

        display_diet.short_description = _('Diet')
