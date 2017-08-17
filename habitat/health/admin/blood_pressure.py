from django.contrib import admin
from habitat.health.models import BloodPressure


@admin.register(BloodPressure)
class BloodPressureAdmin(admin.ModelAdmin):
    list_display = ['datetime', 'astronaut', 'systolic', 'diastolic', 'heart_rate']
    list_filter = ['astronaut']
    date_hierarchy = 'datetime'
