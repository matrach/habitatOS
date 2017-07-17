import datetime
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


def upload_path(instance, filename):
    extension = filename.split('.')[-1]
    today = datetime.date.today()
    return f'reports/img/{today:%Y-%m-%d}_{instance.album.title}.{extension}'


class Album(models.Model):
    STATUSES = [
        ('draft', _('Draft')),
        ('published', _('Published')),
        ('scheduled', _('Scheduled'))]

    status = models.CharField(verbose_name=_('Status'), max_length=30, choices=STATUSES, default='draft')

    created_date = models.DateTimeField(verbose_name=_('Created date'), auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name=_('Modified date'), auto_now=True)
    publish_date = models.DateTimeField(verbose_name=_('Publish Date'), blank=True, null=True, default=timezone.now)

    author = models.ForeignKey(verbose_name=_('Author'), to='auth.User', editable=False, db_index=True, default=None)
    title = models.CharField(verbose_name=_('Title'), max_length=255, db_index=True, default=None)
    slug = models.SlugField(verbose_name=_('Slug'), editable=False, db_index=True, null=True, blank=True, default=None)
    content = models.TextField(verbose_name=_('Content'), null=True, blank=True, default=None)
    tags = models.CharField(verbose_name=_('Tags'), help_text=_('Comma separated tags'), max_length=255, null=True, blank=True, default=None)

    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    is_public = models.BooleanField(verbose_name=_('Is Public?'), default=True)
    date_added = models.DateField(verbose_name=_('Date Aded'), null=True, blank=True)
    order = models.PositiveIntegerField(default=9999)


class Photo(models.Model):
    album = models.ForeignKey(Album)
    file = models.ImageField(upload_to=upload_path)
    description = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.file}'

    class Meta:
        ordering = ['album']
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')

    class Admin(admin.ModelAdmin):
        pass
