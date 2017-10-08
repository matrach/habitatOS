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
    list_display = ['date', 'reporter']
    inlines = [SociodynamicReportEntryInline]
    exclude = ['reporter', 'created', 'updated']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.has_perm('reporting.delete_sociodynamicreport'):
            return queryset
        else:
            return queryset.filter(reporter=request.user)

    def save_model(self, request, obj, form, change):
        obj.reporter = request.user
        super().save_model(request, obj, form, change)
