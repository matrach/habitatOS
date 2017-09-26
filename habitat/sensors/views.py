import logging
from django.http import JsonResponse
from rest_framework import status
from rest_framework import views
from habitat.sensors.models import ZWaveSensor


log = logging.getLogger('habitat.sensor')


class SensorView(views.APIView):
    required_scopes = ['/sensor']

    def get(self, request, *args, **kwargs):
        sensors = [1, 2, 3, 4]
        return JsonResponse(status=status.HTTP_200_OK, data=sensors, safe=False)

    def post(self, request, *args, **kwargs):
        try:
            sensor, created = ZWaveSensor.add(
                datetime=request.data.get('datetime'),
                device=request.data.get('device'),
                type=request.data.get('type'),
                value=request.data.get('value'),
                unit=request.data.get('unit'),
            )

            if created:
                return JsonResponse(status=status.HTTP_201_CREATED, data={'code': 201, 'status': 'Created'}, safe=False)
            else:
                return JsonResponse(status=status.HTTP_200_OK, data={'code': 200, 'status': 'Updated'}, safe=False)

        except Exception as e:
            log.error(e)
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'code': 400, 'status': 'Bad Request'}, safe=False)


