from django.contrib import admin
from habitat.biolab.models import Plant


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ['latin_name', 'species', 'wikipedia_url']
    search_fields = ['latin_name', 'species']
