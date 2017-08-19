from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now


class HabitatModel(models.Model):
    created = models.DateTimeField(
        verbose_name=_('Add Datetime'),
        db_index=True,
        auto_now_add=True)

    modified = models.DateTimeField(
        verbose_name=_('Modified Datetime'),
        db_index=True,
        auto_now=True)

    date = models.CharField(
        verbose_name=_('Date'),
        help_text=_('Lunar Standard Time'),
        max_length=15,
        default=None)

    time = models.TimeField(
        verbose_name=_('Time'),
        help_text=_('Lunar Standard Time'),
        default=now)

    def datetime(self):
        return f'{self.date} ∇ {self.time:%H:%M}'

    datetime.allow_tags = False
    datetime.short_description = _('Datetime')

    class Meta:
        abstract = True


class ReportAstronaut(models.Model):
    reporter = models.ForeignKey(
        verbose_name=_('Astronaut'),
        to='auth.User',
        db_index=True,
        limit_choices_to={'groups__name': 'Astronauts'})

    class Meta:
        abstract = True


class ReportAnyone(models.Model):
    reporter = models.ForeignKey(
        verbose_name=_('Astronaut'),
        db_index=True,
        to='auth.User')

    class Meta:
        abstract = True
