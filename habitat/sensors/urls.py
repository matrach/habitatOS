from django.conf.urls import url
from habitat.sensors import views


urlpatterns = [
    url(r'zwave/', views.ZWaveSensorAPI.as_view()),
    url(r'chart/temperature/', views.TemperatureChartView.as_view()),
]
