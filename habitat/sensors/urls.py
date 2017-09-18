from django.conf.urls import url
from .views import SensorView


urlpatterns = [
    url(r'^data/', SensorView.as_view(), name='data'),
]
