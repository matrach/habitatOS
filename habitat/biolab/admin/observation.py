from django.contrib import admin
from habitat.biolab.models import Observation


@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):
    list_display = ['datetime', 'experiment', 'image']
    search_fields = ['=experiment', '^date', 'notes']
