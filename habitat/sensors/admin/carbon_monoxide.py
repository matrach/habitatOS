from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.sensors.models import CarbonMonoxide


@admin.register(CarbonMonoxide)
class CarbonMonoxideAdmin(HabitatAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    list_display = ['datetime', 'location', 'value']
    list_filter = ['time', 'location']
    search_fields = ['^date', 'value']
