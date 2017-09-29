from django.conf.urls import url
from habitat.sensors import views


urlpatterns = [
    url(r'zwave/$', views.ZWaveSensorAPI.as_view(), name='zwave'),


    url(r'chart/$', views.ChartIndexView.as_view(), name='chart'),
    url(r'chart/battery-level/$', views.BatteryChartView.as_view(), name='chart-battery-level'),
    url(r'chart/powerlevel/$', views.PowerLevelChartView.as_view(), name='chart-powerlevel'),
    url(r'chart/temperature/$', views.TemperatureChartView.as_view(), name='chart-temperature'),
    url(r'chart/luminance/$', views.LuminanceChartView.as_view(), name='chart-luminance'),
    url(r'chart/relative-humidity/$', views.RelativeHumidityChartView.as_view(), name='chart-relative-humidity'),
    url(r'chart/ultraviolet/$', views.UltravioletChartView.as_view(), name='chart-ultraviolet'),
    url(r'chart/burglar/$', views.BurglarChartView.as_view(), name='chart-burglar'),
]
