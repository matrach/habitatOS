import json
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from habitat.sensors.models import Sensor
from habitat.sensors.serializers import SensorSerializer


class UserView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    lookup_fields = ['id']

    def get(self, request, *args, **kwargs):
        sensors = [1, 2, 3]
        return JsonResponse(status=status.HTTP_200_OK, data=sensors, safe=False)

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        print(data)

        if not data:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={})
        else:
            response = JsonResponse(status=status.HTTP_200_OK, data=data)

        return response
