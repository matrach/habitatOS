from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from habitat._common.admin import HabitatAdmin
from django.utils.translation import ugettext_lazy as _
from habitat.reporting.models import Sleep


@admin.register(Sleep)
class SleepAdmin(HabitatAdmin):
    list_display = ['reporter', 'type', 'duration', 'location', 'quality', 'asleep_time', 'wakeup_time']
    list_filter = ['reporter', 'quality', 'sleep_amount', 'sleepy', 'type', 'aid_ear_plugs', 'aid_eye_mask', 'aid_pills']
    search_fields = ['dream']
    readonly_fields = ['duration']
    exclude = ['reporter', 'created', 'updated']
    date_hierarchy = 'wakeup_time'
    ordering = ['-asleep_bedtime']
    formfield_overrides = {models.ManyToManyField: {'widget': CheckboxSelectMultiple}}

    radio_fields = {
        'sleep_amount': admin.HORIZONTAL,
        'quality': admin.HORIZONTAL,
        'sleepy': admin.HORIZONTAL,
        'type': admin.HORIZONTAL,
        'aid_ear_plugs': admin.HORIZONTAL,
        'aid_eye_mask': admin.HORIZONTAL,
        'aid_pills': admin.HORIZONTAL,
    }

    fieldsets = [
        (_('General'), {'fields': ['type', 'location', 'asleep_time', 'wakeup_time', 'sleep_amount', 'quality', 'sleep_quality']}),
        (_('Before Sleep'), {'fields': ['last_activity', 'sleepy', 'sleepy_remarks'], 'classes': ['sleep-report']}),
        (_('Sleep'), {'fields': ['asleep_bedtime', 'asleep_problems', 'impediments_count', 'impediments_remarks', 'aid_ear_plugs', 'aid_eye_mask', 'aid_pills'], 'classes': ['sleep-report']}),
        (_('After Sleep'), {'fields': ['wakeup_reasons', 'getup', 'dream'], 'classes': ['sleep-report']}),
    ]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.has_perm('reporting.delete_sleep'):
            return queryset
        else:
            return queryset.filter(reporter=request.user)

    def save_model(self, request, obj, form, change):
        obj.reporter = request.user
        super().save_model(request, obj, form, change)

    class Media:
        js = ['reporting/js/sleep.js']
