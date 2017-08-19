from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.extravehicular.models import Location


@admin.register(Location)
class LocationAdmin(HabitatAdmin):
    list_display = ['identifier', 'name', 'longitude', 'latitude', 'radius']
