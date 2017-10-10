from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now


class Observation(models.Model):
    experiment = models.ForeignKey(verbose_name=_('Experiment'), to='biolab.Experiment')
    datetime = models.DateTimeField(verbose_name=_('Observation date'), default=now)
    notes = models.TextField(verbose_name=_('Notes'), null=True, blank=True, default=None)
    image = models.ImageField(verbose_name=_('Image'), null=True, blank=True, default=None)

    def __str__(self):
        return f'[{self.datetime}] {self.experiment} {self.notes:.30}'

    class Meta:
        ordering = ['-datetime']
        verbose_name = _('Observation')
        verbose_name_plural = _('Observations')
