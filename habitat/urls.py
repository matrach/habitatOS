import os
from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls'), name='grappelli'),
    url(r'^notepad/', include('habitat.notepad.urls'), name='notepad'),
    url(r'^', admin.site.urls, name='admin'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
