from django.contrib import admin
from habitat.water.models import TechnicalWater


@admin.register(TechnicalWater)
class TechnicalWaterAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    list_display = ['datetime', 'astronaut', 'volume', 'location', 'usage_description']
    date_hierarchy = 'datetime'
    list_filter = ['astronaut', 'datetime', 'location']
