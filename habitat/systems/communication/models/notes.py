from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class PersonalNote(models.Model):
    created_date = models.DateTimeField(verbose_name=_('Created date'), auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name=_('Modified date'), auto_now=True)
    publish_date = models.DateTimeField(verbose_name=_('Publish Date'), default=timezone.now)
    author = models.ForeignKey(verbose_name=_('Author'), to='auth.User')
    content = models.TextField(verbose_name=_('Content'))

    class Admin(admin.ModelAdmin):
        class Media:
            js = [
                '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                '/static/communication/js/tinymce.js',
            ]
