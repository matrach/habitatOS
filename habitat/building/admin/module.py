from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.building.models import Module


@admin.register(Module)
class ModuleAdmin(HabitatAdmin):
    list_display = ['name', 'status', 'hazard', 'width', 'height', 'length', 'plan', 'capacity']
    list_filter = ['status', 'hazard', 'plan', 'capacity']
    list_editable = ['status', 'hazard']
    search_fields = ['name']
    ordering = ['name']
