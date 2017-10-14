from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.reporting.models import SleepQuality


@admin.register(SleepQuality)
class SleepQualityAdmin(HabitatAdmin):
    list_display_links = ['name']
    list_display = ['type', 'name']
    list_filter = ['type']
    list_editable = ['type']
    ordering = ['type', 'name']
