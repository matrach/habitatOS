from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.building.models import Storage


@admin.register(Storage)
class StorageAdmin(HabitatAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    list_display = ['location']
    list_filter = ['location']
    search_fields = ['name']
