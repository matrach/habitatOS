import json
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class SensorView(View):
    http_method_names = ['put']

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        print(data)

        response = JsonResponse(status=201, data={'code': 201, 'status': 'Created', 'message': 'ok'})
        response['Access-Control-Allow-Origin'] = '*'
        return response
