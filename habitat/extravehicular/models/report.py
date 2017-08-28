from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime
from habitat._common.models import ReporterAstronaut


class ReportAttachment(HabitatModel):
    report = models.ForeignKey(
        verbose_name=_('Report'),
        to='extravehicular.Report')

    file = models.FileField(
        verbose_name=_('Attachment'),
        upload_to='report/')

    def __str__(self):
        return f'{self.report} - {self.file}'

    class Meta:
        verbose_name = _('Report Attachment')
        verbose_name_plural = _('Report Attachments')


class Report(HabitatModel, MissionDateTime, ReporterAstronaut):
    STATUS_SUCCESS_FULL = 'success-full'
    STATUS_SUCCESS_PRIMARY = 'success-primary'
    STATUS_SUCCESS_PARTIAL = 'success-partial'
    STATUS_TODO = 'todo'
    STATUS_IN_PROGRESS = 'in-progress'
    STATUS_ABORTED = 'aborted'

    STATUS_CHOICES = [
        (STATUS_SUCCESS_FULL, _('Full Success')),
        (STATUS_SUCCESS_PRIMARY, _('Primary Objectives Done')),
        (STATUS_SUCCESS_PARTIAL, _('Partial Success')),
        (STATUS_TODO, _('To Do')),
        (STATUS_IN_PROGRESS, _('In Progress')),
        (STATUS_ABORTED, _('Aborted')),
    ]

    TYPE_EXPLORATORY = 'exploratory'
    TYPE_EXPERIMENTAL = 'experimental'
    TYPE_OPERATIONAL = 'operational'
    TYPE_EMERGENCY = 'emergency'

    TYPE_CHOICES = [
        (TYPE_EXPLORATORY, _('Exploratory')),
        (TYPE_EXPERIMENTAL, _('Experimental')),
        (TYPE_OPERATIONAL, _('Operational')),
        (TYPE_EMERGENCY, _('Emergency')),
    ]

    location = models.ForeignKey(
        verbose_name=_('Location'),
        to='extravehicular.Location',
        null=True,
        blank=True,
        default=None)

    start = models.TimeField(
        verbose_name=_('Start'),
        blank=True,
        null=True,
        default=None)

    end = models.TimeField(
        verbose_name=_('End'),
        blank=True,
        null=True,
        default=None)

    primary_objectives = models.ManyToManyField(
        verbose_name=_('Primary Objectives'),
        to='extravehicular.Objective',
        related_name='primary_objectives')

    secondary_objectives = models.ManyToManyField(
        verbose_name=_('Secondary Objectives'),
        to='extravehicular.Objective',
        related_name='secondary_objectives',
        blank=True,
        default=None)

    status = models.CharField(
        verbose_name=_('Status'),
        choices=STATUS_CHOICES,
        max_length=30,
        default=STATUS_TODO)

    type = models.CharField(
        verbose_name=_('Type'),
        choices=TYPE_CHOICES,
        max_length=30,
        default=TYPE_OPERATIONAL)

    description = models.TextField(
        verbose_name=_('Description'),
        null=True,
        blank=True,
        default=None)

    contingencies = models.TextField(
        verbose_name=_('Contingencies'),
        null=True,
        blank=True,
        default=None)

    remarks = models.TextField(
        verbose_name=_('Contingencies'),
        null=True,
        blank=True,
        default=None)

    def __str__(self):
        return f'[{self.date}] (location: {self.location}) {self.objectives:.30}'

    class Meta:
        verbose_name = _('Report')
        verbose_name_plural = _('Reports')
