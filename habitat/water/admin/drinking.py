from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.water.models import DrinkingWater


@admin.register(DrinkingWater)
class DrinkingWaterAdmin(HabitatAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    list_display = ['date', 'time', 'reporter', 'volume']
    list_filter = ['reporter']
    ordering = ['-modified']
