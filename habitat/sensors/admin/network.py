from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.sensors.models import Network


@admin.register(Network)
class NetworkAdmin(HabitatAdmin):
    list_display = ['date', 'time', 'location', 'value']
    list_filter = ['created', 'location']
    search_fields = ['^date', 'value']
