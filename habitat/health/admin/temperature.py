from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.health.models import Temperature


@admin.register(Temperature)
class TemperatureAdmin(HabitatAdmin):
    list_display = ['datetime', 'reporter', 'temperature']
    list_filter = ['time', 'reporter']
