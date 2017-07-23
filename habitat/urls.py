from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf.urls.static import static
from filebrowser.sites import site


urlpatterns = [
    url(r'^filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls'), name='grappelli'),
    url(r'^communication/', include('habitat.systems.communication.urls'), name='communication'),
    url(r'^notification/', include('habitat.systems.notification.urls'), name='notification'),
    url(r'^building/light/', include('habitat.building.light.urls'), name='notification'),
    url(r'^drag-and-drop/', include('habitat.drag_and_drop.urls'), name='drag_and_drop'),
    url(r'^', admin.site.urls, name='admin'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
