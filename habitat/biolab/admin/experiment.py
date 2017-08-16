from django.contrib import admin
from habitat.biolab.models import Experiment
from habitat.biolab.models import Observation


class ObservationInline(admin.TabularInline):
    model = Observation
    extra = 1


@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    inlines = [ObservationInline]
    list_display = ['planted_date', 'plant', 'planted_date']
    list_filter = ['cultivation_method']
    search_fields = ['=experiment', '^planted_date', 'plant']
    date_hierarchy = 'planted_date'
