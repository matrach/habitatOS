from django.contrib import admin
from habitat.health.models import PulseOxymetry


@admin.register(PulseOxymetry)
class PulseOxymetryAdmin(admin.ModelAdmin):
    list_display = ['datetime', 'astronaut', 'spo2', 'perfusion_index', 'heart_rate']
    list_filter = ['astronaut', 'spo2']
    date_hierarchy = 'datetime'
