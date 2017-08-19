from django import forms
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDate
from habitat._common.models import ReporterAstronaut


class Sleep(HabitatModel, MissionDate, ReporterAstronaut):
    TYPE_CHOICES = [
        ('sleep', _('Sleep')),
        ('nap', _('Nap'))]

    QUALITY_CHOICES = [
        ('satisfactory', _('Satisfactory')),
        ('slightly-satisfactory', _('Slightly Satisfactory')),
        ('somewhat-satisfactory', _('Somewhat Satisfactory')),
        ('very-unsatisfactory', _('Very Unsatisfactory'))]

    SLEEPY_CHOICES = [
        ('no', _('No')),
        ('mildly', _('Mildly')),
        ('considerably', _('Considerably')),
        ('intensely', _('Intensely'))]

    SLEEP_AMOUNT_CHOICES = [
        ('sufficient', _('Sufficient')),
        ('slightly-sufficient', _('Slightly Sufficient')),
        ('somewhat-sufficient', _('Somewhat Sufficient')),
        ('very-insufficient', _('Very Insufficient'))]

    SLEEPING_AID_CHOICES = [
        (None, _('Undisclosed')),
        (True, _('Yes')),
        (False, _('No')),
    ]

    type = models.CharField(verbose_name=_('Type'), max_length=30, choices=TYPE_CHOICES, default=None)
    location = models.ForeignKey(verbose_name=_('Location'), to='building.Module', limit_choices_to={'status': 'nominal'}, default=1)
    duration = models.DurationField(verbose_name=_('Duration'), null=True, blank=True, default=None)

    # Before sleep
    last_activity = models.CharField(verbose_name=_('What was the last thing you did before going to sleep?'), max_length=255, null=True, blank=True, default=None)
    sleepy = models.CharField(verbose_name=_('Did you feel sleepy during the day?'), choices=SLEEPY_CHOICES, max_length=30, null=True, blank=True, default=None)
    sleepy_remarks = models.PositiveSmallIntegerField(verbose_name=_('If yes, how much?'), help_text=_('Percent of wake time'), validators=[MaxValueValidator(100), MinValueValidator(0)], null=True, blank=True, default=None)

    # Falling asleep
    asleep_bedtime = models.DateTimeField(verbose_name=_('When did you go to bed?'), null=True, blank=True, default=None)
    asleep_time = models.DateTimeField(verbose_name=_('When did you fall asleep?'), default=None)
    asleep_problems = models.CharField(verbose_name=_('If it took you longer than 10 min to fall asleep, what was the reason?'), max_length=255, null=True, blank=True, default=None)

    # Impediments
    impediments_count = models.PositiveSmallIntegerField(verbose_name=_('Did you wake up at night? If you yes, for how long (approx.)?'), help_text=_('Minutes'), null=True, blank=True, default=None)
    impediments_remarks = models.CharField(verbose_name=_('If you woke up during the night, why?'), max_length=255, null=True, blank=True, default=None)

    # Wake Up
    wakeup_time = models.DateTimeField(verbose_name=_('When did you wake up?'), default=now)
    wakeup_reasons = models.CharField(verbose_name=_('What woke you up in the morning?'), help_text=_('Alarm clock / I woke up on my own'), max_length=255, null=True, blank=True, default=None)
    getup = models.DateTimeField(verbose_name=_('When did you get up?'), null=True, blank=True, default=None)

    # Sleeping Aids
    aid_ear_plugs = models.NullBooleanField(verbose_name=_('Did you use ear plugs?'), choices=SLEEPING_AID_CHOICES, null=True, blank=True, default=None)
    aid_eye_mask = models.NullBooleanField(verbose_name=_('Did you use an eye mask?'), choices=SLEEPING_AID_CHOICES, null=True, blank=True, default=None)
    aid_pills = models.NullBooleanField(verbose_name=_('Did you use a sleep pills?'), choices=SLEEPING_AID_CHOICES, null=True, blank=True, default=None)

    # After Sleep
    dream = models.TextField(verbose_name=_('If you remember what was your dream about?'), null=True, blank=True, default=None)
    sleep_amount = models.CharField(verbose_name=_('How would you describe the amount of sleep?'), choices=SLEEP_AMOUNT_CHOICES, max_length=30, default=None)
    quality = models.CharField(verbose_name=_('How would you rate your overall quality of sleep?'), max_length=30, choices=QUALITY_CHOICES, default=None)

    def clean(self):
        if self.asleep_time and self.asleep_time > self.wakeup_time:
            raise forms.ValidationError({'wakeup_time': 'Wake up time must be after falling asleep.'})

        if self.asleep_time and self.wakeup_time:
            self.duration = self.wakeup_time - self.asleep_time

    def __str__(self):
        return f'[{self.asleep_time:%Y-%m-%d %H:%M} for {self.duration}] {self.reporter} Quality: {self.quality}, Location: {self.location}'

    class Meta:
        verbose_name = _('Sleep Log')
        verbose_name_plural = _('Sleep')
