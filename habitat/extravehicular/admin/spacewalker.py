from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.extravehicular.models import Spacewalker


@admin.register(Spacewalker)
class SpacewalkerAdmin(HabitatAdmin):
    list_display = ['activity', 'designation', 'participant']
    list_filter = ['designation', 'participant']
