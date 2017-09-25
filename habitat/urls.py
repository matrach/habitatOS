from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import RedirectView
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    url(r'^api/v1/sensor/', include('habitat.sensors.urls'), name='sensors'),
    url(r'^api/v1/building/', include('habitat.building.urls'), name='building'),
    url(r'^api/v1/communication/', include('habitat.communication.urls'), name='communication'),
    url(r'^api/v1/notification/', include('habitat.notification.urls'), name='notification'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'^api/v1/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/', include_docs_urls(title='HabitatOS API')),
    url(r'^api/$', RedirectView.as_view(permanent=False, url='/api/v1/')),
]

urlpatterns += [
    url(r'^grappelli/', include('grappelli.urls'), name='grappelli'),
    url(r'^', admin.site.urls, name='admin'),
]

