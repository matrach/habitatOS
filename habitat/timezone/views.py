from django.http import JsonResponse
from rest_framework import status
from rest_framework import views
from habitat import timezone


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
