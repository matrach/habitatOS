from django.http import JsonResponse
from rest_framework import status
from rest_framework import permissions
from rest_framework import views
from habitat.sensors.models import Sensor
from habitat.sensors.serializers import SensorSerializer


class SensorView(views.APIView):
    required_scopes = ['/sensor']
    queryset = Sensor.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SensorSerializer

    def get(self, request, *args, **kwargs):
        sensors = [1, 2, 3, 4]
        return JsonResponse(status=status.HTTP_200_OK, data=sensors, safe=False)

    def post(self, request, *args, **kwargs):
        data = SensorSerializer(data=request.data)

        if data.is_valid():
            data.save()
            response = JsonResponse(status=status.HTTP_200_OK, data=data, safe=False)
        else:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={})

        return response
