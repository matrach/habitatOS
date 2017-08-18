from django.contrib import admin
from habitat.health.models import BloodPressure


@admin.register(BloodPressure)
class BloodPressureAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    date_hierarchy = 'datetime'
    list_display = ['datetime', 'astronaut', 'systolic', 'diastolic', 'heart_rate']
    list_filter = ['astronaut']
