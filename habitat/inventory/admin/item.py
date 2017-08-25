from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.inventory.models import Item


@admin.register(Item)
class EdibleAdmin(HabitatAdmin):
    list_display = ['identifier', 'name', 'quantity', 'location']
    list_filter = ['location']
    ordering = ['identifier']
    search_fields = ['^identifier', 'name']
