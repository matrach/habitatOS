from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.reporting.models import Incident


@admin.register(Incident)
class IncidentAdmin(HabitatAdmin):
    list_display = ['start', 'severity', 'location', 'subject']
    list_filter = ['start', 'severity', 'location', 'reporter']
    search_fields = ['subject', 'description']
