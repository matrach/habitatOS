from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.reporting.models import Daily


@admin.register(Daily)
class DailyAdmin(HabitatAdmin):
    list_display = ['date', 'reporter']
    list_filter = ['reporter', 'created']
