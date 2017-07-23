from django.http import JsonResponse
from django.views.generic import View


class LightControlView(View):
    pass


class LightControlTestAPIView(View):

    def get(self, *args, **kwargs):
        return JsonResponse(data=[
            {'red': 255, 'green': 125, 'blue': 125, 'intensity': 1.0, 'miliseconds': 60_000, 'program': 'blink', 'id': 'airlock-bottom-left'},
            {'red':  22, 'green':  11, 'blue':  33, 'intensity': 1.0, 'miliseconds': 60_000, 'program': 'solid', 'id': 'airlock-bottom-right'},
            {'red': 100, 'green': 100, 'blue': 100, 'intensity': 1.0, 'miliseconds': 60_000, 'program': 'blink', 'id': 'airlock-top-left'},
            {'red':   0, 'green':   0, 'blue':   0, 'intensity': 1.0, 'miliseconds': 60_000, 'program': 'fade-in', 'id': 'airlock-top-right'},
            {'red': 255, 'green': 255, 'blue': 255, 'intensity': 1.0, 'miliseconds': 60_000, 'program': 'fade-out', 'id': 'airlock-pipe'},
            {'red': 255, 'green': 125, 'blue': 125, 'intensity': 1.0, 'miliseconds': 60_000, 'program': 'off', 'id': 'dome-bottom'},
            {'red': 255, 'green': 125, 'blue': 125, 'intensity': 1.0, 'miliseconds': 60_000, 'program': 'sequential', 'id': 'dome-top'},
            {'red': 255, 'green': 125, 'blue': 125, 'intensity': 1.0, 'miliseconds': 60_000, 'program': 'solid', 'id': 'dome-across'},
            {'red': 255, 'green': 125, 'blue': 125, 'intensity': 1.0, 'miliseconds': 60_000, 'program': 'solid', 'id': 'operations'},
            {'red': 255, 'green': 125, 'blue': 125, 'intensity': 1.0, 'miliseconds': 60_000, 'program': 'solid', 'id': 'dormitory'},
            {'red': 255, 'green': 125, 'blue': 125, 'intensity': 1.0, 'miliseconds': 60_000, 'program': 'solid', 'id': 'kitchen'},
            {'red': 255, 'green': 125, 'blue': 125, 'intensity': 1.0, 'miliseconds': 60_000, 'program': 'solid', 'id': 'storage'},
            {'red': 255, 'green': 125, 'blue': 125, 'intensity': 1.0, 'miliseconds': 60_000, 'program': 'solid', 'id': 'biolab'},
            {'red': 255, 'green': 125, 'blue': 125, 'intensity': 1.0, 'miliseconds': 60_000, 'program': 'solid', 'id': 'analytic lab'},
            {'red': 255, 'green': 125, 'blue': 125, 'intensity': 1.0, 'miliseconds': 60_000, 'program': 'solid', 'id': 'atrium'},
        ], status=200, safe=False)
