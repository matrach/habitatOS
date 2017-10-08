from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.reporting.models import Mood


@admin.register(Mood)
class MoodAdmin(HabitatAdmin):
    list_display = ['date', 'reporter']
    list_filter = ['modified', 'reporter']
    exclude = ['reporter', 'created', 'updated']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.has_perm('reporting.delete_mood'):
            return queryset
        else:
            return queryset.filter(reporter=request.user)

    def save_model(self, request, obj, form, change):
        obj.reporter = request.user
        super().save_model(request, obj, form, change)
