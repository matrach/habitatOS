from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.health.models import Stool


@admin.register(Stool)
class StoolAdmin(HabitatAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    list_display = ['datetime', 'reporter', 'volume', 'color', 'type', 'abnormalities']
    list_filter = ['time', 'reporter', 'color', 'type', 'abnormalities']
