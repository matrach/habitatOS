from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.sensors.models import CarbonDioxide


@admin.register(CarbonDioxide)
class CarbonDioxideAdmin(HabitatAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    list_display = ['datetime', 'location', 'value']
    list_filter = ['time', 'location']
    search_fields = ['^date', 'value']
