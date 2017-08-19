from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.reporting.models import Repair


@admin.register(Repair)
class RepairAdmin(HabitatAdmin):
    list_display = ['start', 'status', 'object', 'what', 'description', 'location']
    list_filter = ['status', 'size', 'start', 'reporter']
    search_fields = ['what', 'description', 'solution']
    exclude = ['reporter', 'created', 'updated', 'duration']
    date_hierarchy = 'start'
    raw_id_fields = ['object']
    autocomplete_lookup_fields = {'fk': ['object']}
    ordering = ['-modified']
    radio_fields = {
        'status': admin.HORIZONTAL,
        'size': admin.HORIZONTAL}

    def save_model(self, request, obj, form, change):
        obj.reporter = request.user
        super().save_model(request, obj, form, change)
