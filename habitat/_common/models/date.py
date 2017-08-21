from django.db import models
from django.utils.translation import ugettext_lazy as _


class MissionDate(models.Model):
    date = models.CharField(
        verbose_name=_('Mission Date'),
        help_text=_('Lunar Standard Time'),
        max_length=15,
        default=None)

    class Meta:
        abstract = True


class MissionTime(models.Model):
    time = models.TimeField(
            verbose_name=_('Mission Time'),
            help_text=_('Lunar Standard Time'))

    class Meta:
        abstract = True


class MissionDateTime(MissionDate, MissionTime):

    def datetime(self):
        return f'{self.date} ∇ {self.time:%H:%M}'

    datetime.allow_tags = False
    datetime.short_description = _('Datetime')

    class Meta:
        abstract = True
