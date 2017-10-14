from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDate
from habitat._common.models import MissionTime


class Attachment(HabitatModel):
    email = models.ForeignKey(verbose_name=_('Email'), to='communication.Email')
    file = models.FileField(verbose_name=_('Attachment'), upload_to='email/')

    def __str__(self):
        return f'{self.file}'


class Email(HabitatModel, MissionDate, MissionTime):
    to = models.ManyToManyField(verbose_name=_('To'), to='auth.User', db_index=True, related_name='to')
    sender = models.ForeignKey(verbose_name=_('From'), to='auth.User', related_name='sender')
    subject = models.CharField(verbose_name=_('Subject'), max_length=255, db_index=True)
    body = models.TextField(verbose_name=_('Body'), blank=True, null=True, default=None)

    def __str__(self):
        return f'[{self.date} {self.time}] <{self.sender}> {self.subject}'
