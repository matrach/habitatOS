from django.contrib import admin
from habitat.health.models import Temperature


@admin.register(Temperature)
class TemperatureAdmin(admin.ModelAdmin):
    list_display = ['datetime', 'astronaut', 'temperature']
    date_hierarchy = 'datetime'
