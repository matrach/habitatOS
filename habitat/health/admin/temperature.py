from django.contrib import admin
from habitat.health.models import Temperature


@admin.register(Temperature)
class TemperatureAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    date_hierarchy = 'datetime'
    list_display = ['datetime', 'astronaut', 'temperature']
    date_hierarchy = 'datetime'
