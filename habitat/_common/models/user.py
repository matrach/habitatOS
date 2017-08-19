from django.db import models
from django.utils.translation import ugettext_lazy as _


class ReporterAstronaut(models.Model):
    reporter = models.ForeignKey(
        verbose_name=_('Astronaut'),
        to='auth.User',
        db_index=True,
        limit_choices_to={'groups__name': 'Astronauts'})

    class Meta:
        abstract = True


class ReporterAnyone(models.Model):
    reporter = models.ForeignKey(
        verbose_name=_('Astronaut'),
        db_index=True,
        to='auth.User')

    class Meta:
        abstract = True
