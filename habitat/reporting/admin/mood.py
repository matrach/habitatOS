from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.reporting.models import Mood


@admin.register(Mood)
class MoodAdmin(HabitatAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    list_display = ['day', 'reporter', 'stress', 'mood', 'day_quality', 'productivity']
    list_filter = ['reporter', 'stress', 'mood', 'day_quality', 'productivity']
    exclude = ['reporter', 'created', 'updated']
    date_hierarchy = 'day'
    ordering = ['-day']
    radio_fields = {
        'stress': admin.HORIZONTAL,
        'mood': admin.HORIZONTAL,
        'day_quality': admin.HORIZONTAL,
        'productivity': admin.HORIZONTAL}

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.has_perm('reporting.delete_mood'):
            return queryset
        else:
            return queryset.filter(reporter=request.user)

    def save_model(self, request, obj, form, change):
        obj.reporter = request.user
        super().save_model(request, obj, form, change)
