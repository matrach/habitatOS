from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.extravehicular.models import Contingency


@admin.register(Contingency)
class ContingencyAdmin(HabitatAdmin):
    list_display = ['identifier', 'severity', 'name']
    list_filter = ['severity']
