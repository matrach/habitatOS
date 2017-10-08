from django.views.generic import TemplateView
from habitat.timezone import get_timezone


class MissionClockView(TemplateView):
    template_name = 'dashboard/mission-clock.html'

    def get_context_data(self, **kwargs):
        timezone = get_timezone()
        return {
            'datetime': timezone.datetime,
            'date': timezone.date,
            'time': timezone.time,
            'timezone': timezone.NAME,
        }


class MissionScheduleView(TemplateView):
    template_name = 'dashboard/mission-schedule.html'
