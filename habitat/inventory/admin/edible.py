from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.inventory.models import Edible


@admin.register(Edible)
class EdibleAdmin(HabitatAdmin):
    list_display = ['code', 'product', 'quantity']
    ordering = ['code']
    search_fields = ['^code', '^product__name']
