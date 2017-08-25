import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _


def lunar_standard_time():
    begin = datetime.date(1969, 7, 21)
    today = datetime.date.today()
    year = int((today-begin).days / 365 + 2)
    date = today - datetime.timedelta(days=29)
    return f'{year}-{date.month:02}-{date.day}'


class MissionDate(models.Model):
    date = models.CharField(
        verbose_name=_('Mission Date'),
        help_text=_('Lunar Standard Time'),
        max_length=15,
        default=lunar_standard_time)

    class Meta:
        abstract = True


class MissionTime(models.Model):
    time = models.TimeField(
        verbose_name=_('Mission Time'),
        help_text=_('Lunar Standard Time'),
        default=None)

    class Meta:
        abstract = True


class MissionDateTime(MissionDate, MissionTime):

    def datetime(self):
        return f'{self.date} ∇ {self.time:%H:%M}'

    datetime.allow_tags = False
    datetime.short_description = _('Datetime')

    class Meta:
        abstract = True
