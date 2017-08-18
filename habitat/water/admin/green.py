from django.contrib import admin
from habitat.water.models import GreenWater


@admin.register(GreenWater)
class GreenWaterAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    list_display = ['datetime', 'astronaut', 'volume', 'usage_description']
    date_hierarchy = 'datetime'
