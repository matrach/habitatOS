from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.building.models import Storage


@admin.register(Storage)
class StorageAdmin(HabitatAdmin):
    list_display = ['location', 'name']
    list_filter = ['location']
    search_fields = ['name']
    ordering = ['name']
