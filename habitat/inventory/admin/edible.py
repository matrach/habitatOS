from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.inventory.models import Edible


@admin.register(Edible)
class EdibleAdmin(HabitatAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    list_display = ['code', 'product', 'quantity']
    ordering = ['code']
    search_fields = ['^code', '^product__name']
