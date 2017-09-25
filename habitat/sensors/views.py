from django.http import JsonResponse
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import status
from rest_framework import views
from habitat.sensors.models import ZWaveSensor


class SensorView(views.APIView):
    required_scopes = ['/sensor']

    def get(self, request, *args, **kwargs):
        sensors = [1, 2, 3, 4]
        return JsonResponse(status=status.HTTP_200_OK, data=sensors, safe=False)

    def post(self, request, *args, **kwargs):
        return JsonResponse(status=status.HTTP_200_OK, data=request.data, safe=False)

