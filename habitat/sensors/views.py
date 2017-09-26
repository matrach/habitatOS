import logging
from django.http import JsonResponse
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework import views
import plotly.offline as plt
import plotly.graph_objs as graph
from habitat.sensors.models import ZWaveSensor


log = logging.getLogger('habitat.sensor')


class ZWaveSensorAPI(views.APIView):
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


class TemperatureChartView(TemplateView):
    template_name = 'sensors/graph.html'
    queryset = ZWaveSensor.objects.filter(type=ZWaveSensor.TYPE_TEMPERATURE, unit=ZWaveSensor.UNIT_CELSIUS).order_by('datetime')

    def get_trace(self, device, color='#00f', legend=None):
        data = self.queryset.filter(device=device)

        return graph.Scatter(
            x=list(data.values_list('datetime', flat=True)),
            y=list(data.values_list('value', flat=True)),
            marker={'color': color, 'symbol': 104, 'size': 10},
            mode='lines',
            name=legend)

    def get_context_data(self, **kwargs):
        traces = [
            self.get_trace(device='c1344062-2', color='#f00', legend='2'),
            self.get_trace(device='c1344062-3', color='#00f', legend='3'),
            self.get_trace(device='c1344062-4', color='#0f0', legend='hydroponics'),
            self.get_trace(device='c1344062-5', color='#ff0', legend='4'),
        ]

        figure = graph.Figure(
            data=graph.Data(traces),
            layout=graph.Layout(
                title='Temperature',
                xaxis={'title': 'Time [t]', 'showgrid': False, 'autorange': True, 'type': 'date', 'rangeslider': {}},
                yaxis={'title': 'Temperature [°C]'}))

        return {'graph': plt.plot(figure, auto_open=False, output_type='div', show_link=False)}