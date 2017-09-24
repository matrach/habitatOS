from django.conf.urls import url
from habitat.sensors import views


urlpatterns = [
    url(r'z-wave/', views.UserView.as_view()),
]
