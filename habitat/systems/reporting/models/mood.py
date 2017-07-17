from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.contrib import admin


class Mood(models.Model):
    MOOD_CHOICES = [
        ('very-high', _('Very High')),
        ('high', _('High')),
        ('normal', _('Normal')),
        ('low', _('Low')),
        ('very-low', _('Very Low'))]

    QUALITY_CHOICES = [
        ('very-good', _('Very Good')),
        ('good', _('Good')),
        ('average', _('Average')),
        ('bad', _('Bad')),
        ('very-bad', _('Very Bad'))]

    astronaut = models.ForeignKey(verbose_name=_('Astronaut'), to='auth.User', limit_choices_to={'groups__name': 'Astronauts'})
    created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'), auto_now=True)

    day = models.DateField(verbose_name=_('Report About Day'), default=now)
    stress = models.CharField(verbose_name=_('Stress'), max_length=30, choices=MOOD_CHOICES, default=None)
    mood = models.CharField(verbose_name=_('Mood'), max_length=30, choices=MOOD_CHOICES, default=None)
    day_quality = models.CharField(verbose_name=_('Day Quality'), max_length=30, choices=QUALITY_CHOICES, default=None)
    productivity = models.CharField(verbose_name=_('Productivity'), max_length=30, choices=MOOD_CHOICES, default=None)
    remarks = models.TextField(verbose_name=_('Remarks'), blank=True, default=None)

    def __str__(self):
        return f'[{self.day:%Y-%m-%d}] {self.astronaut}'

    class Meta:
        ordering = ['-day']
        verbose_name = _('Mood Report')
        verbose_name_plural = _('Mood Reports')

    class Admin(admin.ModelAdmin):
        change_list_template = 'admin/change_list_filter_sidebar.html'
        list_display = ['day', 'astronaut', 'stress', 'mood', 'day_quality', 'productivity']
        list_filter = ['astronaut', 'stress', 'mood', 'day_quality', 'productivity']
        exclude = ['astronaut', 'created', 'updated']
        radio_fields = {
            'stress': admin.HORIZONTAL,
            'mood': admin.HORIZONTAL,
            'day_quality': admin.HORIZONTAL,
            'productivity': admin.HORIZONTAL}

        def get_queryset(self, request):
            queryset = super().get_queryset(request)

            if request.user.has_perm('reporting.delete_mood'):
                return queryset
            else:
                return queryset.filter(astronaut=request.user)

        def save_model(self, request, obj, form, change):
            obj.astronaut = request.user
            super().save_model(request, obj, form, change)
