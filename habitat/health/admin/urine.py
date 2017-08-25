from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.health.models import Urine


@admin.register(Urine)
class UrineAdmin(HabitatAdmin):
    list_display = ['datetime', 'reporter', 'volume', 'color', 'turbidity', 'ph']
    list_filter = ['time', 'reporter', 'color', 'turbidity', 'ph']
