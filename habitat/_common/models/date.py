from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat.timezone import get_timezone


timezone = get_timezone()


class MissionDate(models.Model):

    date = models.CharField(
        verbose_name=_(timezone.DATE_VERBOSE_NAME),
        help_text=_(timezone.DATE_HELP_TEXT),
        max_length=15,
        default=timezone.date)

    class Meta:
        abstract = True


class MissionTime(models.Model):
    time = models.TimeField(
        verbose_name=_(timezone.TIME_VERBOSE_NAME),
        help_text=_(timezone.TIME_HELP_TEXT),
        default=timezone.time)

    class Meta:
        abstract = True


class MissionDateTime(MissionDate, MissionTime):

    def datetime(self):
        return timezone.datetime

    datetime.allow_tags = False
    datetime.short_description = _(timezone.DATETIME_VERBOSE_NAME)

    class Meta:
        abstract = True
