from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.contrib import admin


class Disease(models.Model):
    astronaut = models.ForeignKey(
        to='auth.User',
        limit_choices_to={'groups__name': 'Astronauts'})

    datetime_start = models.DateTimeField(
        verbose_name=_('Start Datetime'),
        default=now)

    datetime_end = models.DateTimeField(
        verbose_name=_('End Datetime'),
        blank=False,
        null=False)

    icd10 = models.CharField(
        verbose_name=_('ICD-10'),
        max_length=50)

    sympthoms = models.TextField(
        blank=False,
        null=False)

    def __str__(self):
        return f'[{self.datetime_start:%Y-%m-%d}] {self.astronaut} ICD-10: {self.icd10}, Sympthoms: {self.sympthoms:.30}'

    class Meta:
        ordering = ['-datetime_start']

    class Admin(admin.ModelAdmin):
        list_display = ['datetime_start', 'datetime_end', 'astronaut', 'icd10']
        list_filter = ['astronaut', 'icd10']
        search_fields = ['sympthoms']
