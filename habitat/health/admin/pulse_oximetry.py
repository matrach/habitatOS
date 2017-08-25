from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.health.models import PulseOxymetry


@admin.register(PulseOxymetry)
class PulseOxymetryAdmin(HabitatAdmin):
    list_display = ['datetime', 'reporter', 'spo2', 'perfusion_index', 'heart_rate']
    list_filter = ['reporter', 'spo2']
