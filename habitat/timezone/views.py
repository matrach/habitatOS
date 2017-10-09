import datetime

from django.http import JsonResponse
from django.views import generic
from django.utils.timezone import now
from rest_framework import status
from rest_framework import views
from habitat import timezone
from habitat.timezone.models import MartianStandardTime


class LunarStandardTimeAPI(views.APIView):
    def get(self, request, *args, **kwargs):
        """
        Return a dict with Lunar Standard Time.
        """
        data = timezone.LunarStandardTime().get_time_dict()
        return JsonResponse(status=status.HTTP_200_OK, data=data)


class MartianStandardTimeAPI(views.APIView):
    def get(self, request, *args, **kwargs):
        """
        Return a dict with Marian Standard Time.
        """
        data = timezone.MartianStandardTime().get_time_dict()
        return JsonResponse(status=status.HTTP_200_OK, data=data)


class MartianStandardTimeConverterView(generic.TemplateView):
    template_name = 'timezone/martian-standard-time-converter.html'

    def get_context_data(self, *args, **kwargs):
        if not self.request.GET:
            return {
                'utc': now(),
                'mst': MartianStandardTime()
            }

        if self.request.GET.get('utc-date'):
            date = self.request.GET['utc-date']
            time = self.request.GET['utc-time']
            utc = datetime.datetime.strptime(f'{date} {time}', '%Y-%m-%d %H:%M')
            mst = MartianStandardTime().get_time_dict(from_datetime=utc)

            return {
                'result': True,
                'utc': utc,
                'mst': mst,
            }
