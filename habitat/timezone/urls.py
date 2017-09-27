from django.conf.urls import url
from habitat.timezone import views


urlpatterns = [
    url(r'lunar-standard-time/', views.LunarStandardTimeAPI.as_view(), name='lunar-standard-time'),
]
