from django.contrib import admin
from habitat.health.models import Disease


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ['datetime_start', 'datetime_end', 'astronaut', 'icd10']
    list_filter = ['astronaut', 'icd10']
    search_fields = ['sympthoms']
