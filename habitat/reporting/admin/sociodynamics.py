from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat._common.admin import HabitatTabularInline
from habitat.reporting.models import SociodynamicReport
from habitat.reporting.models import SociodynamicReportEntry


class SociodynamicReportEntryInline(HabitatTabularInline):
    model = SociodynamicReportEntry
    extra = 5
    max_num = 5
    min_num = 5


@admin.register(SociodynamicReport)
class SociodynamicReportAdmin(HabitatAdmin):
    inlines = [SociodynamicReportEntryInline]
