from django.conf.urls import url

from .views import LightControlTestAPIView

urlpatterns = [
    url(r'^lightning/test/', LightControlTestAPIView.as_view(), name='test'),
]
