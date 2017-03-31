from django.conf.urls import url
from .views import *


app_name = 'communication'

urlpatterns = [
    url(r'^diary/(?P<slug>[-\w]{1,255})/', Diary.as_view(), name='diary'),
]
