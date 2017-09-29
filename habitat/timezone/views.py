from django.http import JsonResponse
from rest_framework import status
from rest_framework import views
from habitat.timezone import LunarStandardTime


class LunarStandardTimeAPI(views.APIView):
    def get(self, request, *args, **kwargs):
        data = LunarStandardTime().get_time_dict()
        return JsonResponse(status=status.HTTP_200_OK, data=data)
