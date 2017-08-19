from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.reporting.models import Incident


@admin.register(Incident)
class IncidentAdmin(HabitatAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    date_hierarchy = 'datetime_start'
    list_display = ['datetime_start', 'severity', 'location', 'subject']
    list_filter = ['datetime_start', 'severity', 'location', 'reporter']
    search_fields = ['subject', 'description']
    ordering = ['-modified']
