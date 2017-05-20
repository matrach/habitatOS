from django.contrib import admin
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


class Figure(models.Model):
    diary_entry = models.ForeignKey(verbose_name=_('Entry'), to='communication.DiaryEntry')
    image = models.ImageField(verbose_name=_('Image'))
    caption = models.CharField(verbose_name=_('Caption'), max_length=255)

    def __str__(self):
        return f'{self.caption}'


class FigureInline(admin.TabularInline):
    model = Figure


class DiaryEntry(models.Model):
    STATUSES = [
        ('draft', _('Draft')),
        ('published', _('Published')),
    ]

    status = models.CharField(verbose_name=_('Status'), max_length=30, choices=STATUSES, default='draft')
    created_date = models.DateTimeField(verbose_name=_('Created date'), auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name=_('Modified date'), auto_now=True)
    publish_date = models.DateTimeField(verbose_name=_('Publish Date'), default=timezone.now, db_index=True)
    author = models.ForeignKey(verbose_name=_('Author'), to='auth.User', editable=False, db_index=True)
    title = models.CharField(verbose_name=_('Title'), max_length=255, db_index=True)
    slug = models.SlugField(verbose_name=_('Slug'), editable=False, db_index=True)
    content = models.TextField(verbose_name=_('Content'))
    tags = models.CharField(verbose_name=_('Tags'), help_text=_('Comma separated tags'), max_length=255, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('communication:diary', args=[self.slug])

    def __str__(self):
        return f'[{self.publish_date:%Y-%m-%d}] ({self.status}) {self.author}: {self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Admin(admin.ModelAdmin):
        inlines = [FigureInline]
        list_display = ['publish_date', 'author', 'title']
        search_fields = ['title']
        list_filter = ['author']

        def save_model(self, request, obj, form, change):
            obj.author = request.user
            obj.save()

        class Media:
            js = [
                '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                '/static/communication/js/tinymce.js']
