from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat._common.admin import HabitatTabularInline
from habitat.extravehicular.models import Activity
from habitat.extravehicular.models import Spacewalker


class SpacewalkerInline(HabitatTabularInline):
    model = Spacewalker
    extra = 3


@admin.register(Activity)
class ActivityAdmin(HabitatAdmin):
    list_display = ['date', 'location', 'airlock_enter', 'eva_start', 'eva_end', 'airlock_exit']
    list_filter = ['location']
    inlines = [SpacewalkerInline]
    raw_id_fields = ['contingencies', 'tools']
    autocomplete_lookup_fields = {'m2m': ['contingencies', 'tools']}
