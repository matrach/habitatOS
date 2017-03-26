from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin


urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls'), name='grappelli'),
    url(r'^notepad/', include('habitat.notepad.urls'), name='notepad'),
    url(r'^', admin.site.urls, name='admin'),
]
