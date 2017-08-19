from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.health.models import BloodPressure


@admin.register(BloodPressure)
class BloodPressureAdmin(HabitatAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    list_display = ['datetime', 'reporter', 'systolic', 'diastolic', 'heart_rate']
    list_filter = ['reporter']
