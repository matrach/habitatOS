from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.extravehicular.models import Activity


@admin.register(Activity)
class ActivityAdmin(HabitatAdmin):
    list_display = ['datetime', 'start', 'end', 'location']
    list_filter = ['location']
