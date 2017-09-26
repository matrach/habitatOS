from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.sensors.models import ZWaveSensor


@admin.register(ZWaveSensor)
class ZWaveSensorAdmin(HabitatAdmin):
    change_list_template = 'sensors/change_list_charts.html'
    list_display = ['date', 'time', 'type', 'device', 'value', 'unit']
    list_filter = ['created', 'type', 'unit', 'device']
    search_fields = ['^date', 'device']
