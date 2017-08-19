from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.reporting.models import Waste


@admin.register(Waste)
class WasteAdmin(HabitatAdmin):
    list_display = ['date', 'type', 'weight']
    list_filter = ['type']
