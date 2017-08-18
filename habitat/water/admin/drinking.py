from django.contrib import admin
from habitat.water.models import DrinkingWater


@admin.register(DrinkingWater)
class DrinkingWaterAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    list_display = ['datetime', 'astronaut', 'volume']
    date_hierarchy = 'datetime'
    list_filter = ['astronaut', 'datetime']
