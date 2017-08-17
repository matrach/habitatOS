from django.contrib import admin
from habitat.building.models import Module


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    list_display = ['name', 'status', 'hazard', 'width', 'height', 'length', 'plan', 'capacity']
    list_filter = ['status', 'hazard', 'plan', 'capacity']
    list_editable = ['status', 'hazard']
    search_fields = ['name']
