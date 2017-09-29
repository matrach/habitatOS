from django.conf.urls import url
from habitat.dashboard import views


urlpatterns = [
    url(r'^clock/', views.MissionClockView.as_view(), name='clock'),
]
