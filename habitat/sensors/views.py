import logging
from django.http import JsonResponse
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework import views
import plotly.offline as plt
import plotly.graph_objs as graph
from habitat.sensors.models import ZWaveSensor


log = logging.getLogger('habitat.sensor')


class UserView(views.APIView):
    required_scopes = ['/sensor']

    def get(self, request, *args, **kwargs):
        """
        List of all available sensors configuration
        """
        sensors = [
            dict(device='c1344062-2', color='#00f', legend='atrium'),
            dict(device='c1344062-3', color='#0f0', legend='analytic-lab'),
            dict(device='c1344062-4', color='#0ff', legend='operations'),
            dict(device='c1344062-5', color='#08f', legend='toilet'),
            dict(device='c1344062-6', color='#f00', legend='dormitory'),
            dict(device='c1344062-7', color='#f0f', legend='storage'),
            dict(device='c1344062-8', color='#ff0', legend='kitchen'),
            dict(device='c1344062-9', color='#555', legend='biolab')]

        return JsonResponse(status=status.HTTP_200_OK, data=sensors, safe=False)


class ZWaveSensorAPI(views.APIView):
    required_scopes = ['/sensor']

    def get(self, request, *args, **kwargs):
        """
        List of all available sensors configuration
        """
        sensors = [
            dict(device='c1344062-2', color='#00f', legend='atrium'),
            dict(device='c1344062-3', color='#0f0', legend='analytic-lab'),
            dict(device='c1344062-4', color='#0ff', legend='operations'),
            dict(device='c1344062-5', color='#08f', legend='toilet'),
            dict(device='c1344062-6', color='#f00', legend='dormitory'),
            dict(device='c1344062-7', color='#f0f', legend='storage'),
            dict(device='c1344062-8', color='#ff0', legend='kitchen'),
            dict(device='c1344062-9', color='#555', legend='biolab')]

        return JsonResponse(status=status.HTTP_200_OK, data=sensors, safe=False)

    def post(self, request, *args, **kwargs):
        """
        Add sensor measurement to database
        """
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


class ChartIndexView(views.APIView):
    required_scopes = ['/sensor']

    def get(self, request, *args, **kwargs):
        """
        List all available charts.
        """
        schema = 'https' and request.is_secure() or 'http'
        domain = request.get_host()
        response = []

        for url, name in ZWaveSensor.TYPE_CHOICES:
            response.append({
                'name': name,
                'url': f'{schema}://{domain}/api/v1/sensor/chart/{url}/'
            })

        return JsonResponse(status=200, data=response, safe=False)


class ChartView(TemplateView):
    template_name = 'sensors/graph.html'

    def get_trace(self, device, color='#00f', legend=None):
        data = self.queryset.filter(device=device)

        return graph.Scatter(
            x=list(data.values_list('datetime', flat=True)),
            y=list(data.values_list('value', flat=True)),
            marker={'color': color, 'symbol': 104, 'size': 10},
            mode='lines',
            name=legend)

    def get_taces(self):
        return [
            dict(device='c1344062-2', color='#00f', legend='atrium'),
            dict(device='c1344062-3', color='#0f0', legend='analytic-lab'),
            dict(device='c1344062-4', color='#0ff', legend='operations'),
            dict(device='c1344062-5', color='#08f', legend='toilet'),
            dict(device='c1344062-6', color='#f00', legend='dormitory'),
            dict(device='c1344062-7', color='#f0f', legend='storage'),
            dict(device='c1344062-8', color='#ff0', legend='kitchen'),
            dict(device='c1344062-9', color='#555', legend='biolab')]

    def get_context_data(self):
        figure = graph.Figure(
            data=graph.Data(self.get_taces()),
            layout=graph.Layout(
                title=self.title,
                xaxis={'title': self.title_x, 'showgrid': False, 'autorange': True, 'type': 'date', 'rangeslider': {}},
                yaxis={'title': self.title_y}))

        return {'graph': plt.plot(figure, auto_open=False, output_type='div', show_link=False)}


class BatteryChartView(ChartView):
    queryset = ZWaveSensor.objects.filter(type=ZWaveSensor.TYPE_BATTERY_LEVEL).order_by('datetime')
    title = 'Battery Level'
    title_x = 'Time [UTC]'
    title_y = 'Battery Level [%]'


class PowerLevelChartView(ChartView):
    queryset = ZWaveSensor.objects.filter(type=ZWaveSensor.TYPE_POWER_LEVEL).order_by('datetime')
    title = 'PowerLevel'
    title_x = 'Time [UTC]'
    title_y = 'Power Level [dB]'


class TemperatureChartView(ChartView):
    queryset = ZWaveSensor.objects.filter(type=ZWaveSensor.TYPE_TEMPERATURE, unit=ZWaveSensor.UNIT_CELSIUS).order_by('datetime')
    title = 'Temperature'
    title_x = 'Time [UTC]'
    title_y = 'Temperature [°C]'


class LuminanceChartView(ChartView):
    queryset = ZWaveSensor.objects.filter(type=ZWaveSensor.TYPE_LUMINANCE).order_by('datetime')
    title = 'Luminance'
    title_x = 'Time [UTC]'
    title_y = 'Luminance [lux]'


class RelativeHumidityChartView(ChartView):
    queryset = ZWaveSensor.objects.filter(type=ZWaveSensor.TYPE_RELATIVE_HUMIDITY).order_by('datetime')
    title = 'Relative Humidity'
    title_x = 'Time [UTC]'
    title_y = 'Humidity [%]'


class UltravioletChartView(ChartView):
    queryset = ZWaveSensor.objects.filter(type=ZWaveSensor.TYPE_ULTRAVIOLET).order_by('datetime')
    title = 'Ultraviolet'
    title_x = 'Time [UTC]'
    title_y = 'Ultraviolet'


class BurglarChartView(ChartView):
    queryset = ZWaveSensor.objects.filter(type=ZWaveSensor.TYPE_BURGLAR).order_by('datetime')
    title = 'Burglar'
    title_x = 'Time [UTC]'
    title_y = 'Burglar'
