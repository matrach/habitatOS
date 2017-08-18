from django.contrib import admin
from habitat.health.models import Urine


@admin.register(Urine)
class UrineAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    date_hierarchy = 'datetime'
    list_display = ['datetime', 'astronaut', 'volume', 'color', 'turbidity', 'ph']
    list_filter = ['datetime', 'astronaut', 'color', 'turbidity', 'ph']
