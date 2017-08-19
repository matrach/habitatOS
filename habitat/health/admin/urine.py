from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.health.models import Urine


@admin.register(Urine)
class UrineAdmin(HabitatAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    list_display = ['datetime', 'reporter', 'volume', 'color', 'turbidity', 'ph']
    list_filter = ['time', 'reporter', 'color', 'turbidity', 'ph']
