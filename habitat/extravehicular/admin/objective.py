from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.extravehicular.models import Objective


@admin.register(Objective)
class ObjectiveAdmin(HabitatAdmin):
    list_display = ['identifier', 'estimated_duration', 'location', 'objective']
    list_filter = ['location']
