from django.conf.urls import url
from habitat.timezone import views


urlpatterns = [
    url(r'lunar-standard-time/$', views.LunarStandardTimeAPI.as_view(), name='lunar-standard-time'),

    url(r'martian-standard-time/$', views.MartianStandardTimeAPI.as_view(), name='martian-standard-time'),
    url(r'martian-standard-time/converter/$', views.MartianStandardTimeConverterView.as_view(), name='martian-standard-time-converter'),
]
