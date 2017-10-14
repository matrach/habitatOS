from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.reporting.models import SleepQuality


@admin.register(SleepQuality)
class SleepQualityAdmin(HabitatAdmin):
    list_display = ['name']
