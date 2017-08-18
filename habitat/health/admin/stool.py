from django.contrib import admin
from habitat.health.models import Stool


@admin.register(Stool)
class StoolAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    date_hierarchy = 'datetime'
    list_display = ['datetime', 'astronaut', 'volume', 'color', 'type', 'abnormalities']
    list_filter = ['datetime', 'astronaut', 'color', 'type', 'abnormalities']
