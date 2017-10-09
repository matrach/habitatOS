from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from habitat._common.models import HabitatModel


class PersonalNote(HabitatModel):
    created_date = models.DateTimeField(verbose_name=_('Created date'), auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name=_('Modified date'), auto_now=True)
    publish_date = models.DateTimeField(verbose_name=_('Publish Date'), default=timezone.now)
    author = models.ForeignKey(verbose_name=_('Author'), to='auth.User')
    content = models.TextField(verbose_name=_('Content'))

    def __str__(self):
        return f'[{self.date} {self.time}] {self.author} {self.content:.30}'

    class Meta:
        ordering = ['-modified_date']
        verbose_name = _('Personal Note')
        verbose_name_plural = _('Personal Notes')

    class Admin(admin.ModelAdmin):
        list_display = ['modified_date', 'publish_date', 'author']
        search_fields = ['content']
        list_filter = ['author']
        date_hierarchy = 'publish_date'

        class Media:
            js = [
                '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                '/static/communication/js/tinymce.js']
