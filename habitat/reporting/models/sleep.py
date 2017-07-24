from django import forms
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.contrib import admin


class Sleep(models.Model):
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

    astronaut = models.ForeignKey(verbose_name=_('Astronaut'), to='auth.User', limit_choices_to={'groups__name': 'Astronauts'})
    created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'), auto_now=True)
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
        return f'[{self.asleep_time:%Y-%m-%d %H:%M} for {self.duration}] {self.astronaut} Quality: {self.quality}, Location: {self.location}'

    class Meta:
        ordering = ['-asleep_bedtime']
        verbose_name = _('Sleep Log')
        verbose_name_plural = _('Sleep Logbook')

    class Admin(admin.ModelAdmin):
        change_list_template = 'admin/change_list_filter_sidebar.html'
        list_display = ['astronaut', 'type', 'duration', 'location', 'quality', 'asleep_time', 'wakeup_time']
        list_filter = ['astronaut', 'quality', 'sleep_amount', 'sleepy', 'type', 'aid_ear_plugs', 'aid_eye_mask', 'aid_pills']
        search_fields = ['dream']
        readonly_fields = ['duration']
        exclude = ['astronaut', 'created', 'updated']
        date_hierarchy = 'wakeup_time'
        # raw_id_fields = ['astronaut']
        # autocomplete_lookup_fields = {'fk': ['astronaut']}

        radio_fields = {
            'sleep_amount': admin.HORIZONTAL,
            'quality': admin.HORIZONTAL,
            'sleepy': admin.HORIZONTAL,
            'type': admin.HORIZONTAL,
            'aid_ear_plugs': admin.HORIZONTAL,
            'aid_eye_mask': admin.HORIZONTAL,
            'aid_pills': admin.HORIZONTAL}

        fieldsets = [
            (_('General'), {'fields': ['type', 'location', 'asleep_time', 'wakeup_time', 'sleep_amount', 'quality']}),
            (_('Before Sleep'), {'fields': ['last_activity', 'sleepy', 'sleepy_remarks']}),
            (_('Sleep'), {'fields': ['asleep_bedtime', 'asleep_problems', 'impediments_count', 'impediments_remarks', 'aid_ear_plugs', 'aid_eye_mask', 'aid_pills']}),
            (_('After Sleep'), {'fields': ['wakeup_reasons', 'getup', 'dream']})]

        def get_queryset(self, request):
            queryset = super().get_queryset(request)

            if request.user.has_perm('reporting.delete_mood'):
                return queryset
            else:
                return queryset.filter(astronaut=request.user)

        def save_model(self, request, obj, form, change):
            obj.astronaut = request.user
            super().save_model(request, obj, form, change)
