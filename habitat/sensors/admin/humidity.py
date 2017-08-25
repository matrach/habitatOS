from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.sensors.models import Humidity


@admin.register(Humidity)
class HumidityAdmin(HabitatAdmin):
    list_display = ['datetime', 'location', 'value']
    list_filter = ['created', 'location']
    search_fields = ['^date', 'value']
