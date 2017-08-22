from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.extravehicular.models import Report


@admin.register(Report)
class ReportAdmin(HabitatAdmin):
    list_display = ['datetime', 'start', 'end', 'location']
    list_filter = ['location']
    raw_id_fields = ['primary_objectives', 'secondary_objectives']
    autocomplete_lookup_fields = {'m2m': ['primary_objectives', 'secondary_objectives']}
