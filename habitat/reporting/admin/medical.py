from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.reporting.models import Medical


@admin.register(Medical)
class MedicalAdmin(HabitatAdmin):
    list_display = ['date']
    list_filter = []
