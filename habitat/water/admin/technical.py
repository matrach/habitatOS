from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.water.models import TechnicalWater


@admin.register(TechnicalWater)
class TechnicalWaterAdmin(HabitatAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    list_display = ['datetime', 'reporter', 'volume', 'location', 'usage_description']
    date_hierarchy = 'modified'
    list_filter = ['reporter', 'location', 'time']
    ordering = ['-modified']
