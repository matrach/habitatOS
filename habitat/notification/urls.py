from django.conf.urls import url
from .views import NotificationClientView
from .views import NotificationServerView


urlpatterns = [
    url(r'^server/', NotificationServerView.as_view(), name='server'),
    url(r'^client/', NotificationClientView.as_view(), name='client'),
]
