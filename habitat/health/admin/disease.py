from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.health.models import Disease


@admin.register(Disease)
class DiseaseAdmin(HabitatAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    list_display = ['datetime_start', 'datetime_end', 'reporter', 'icd10']
    list_filter = ['reporter', 'icd10']
    search_fields = ['symptoms']
