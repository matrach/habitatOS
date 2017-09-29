from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import RedirectView
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer


urlpatterns = [
    url(r'^api/v1/building/', include('habitat.building.urls', namespace='building')),
    url(r'^api/v1/communication/', include('habitat.communication.urls', namespace='communication')),
    url(r'^api/v1/dashboard/', include('habitat.dashboard.urls', namespace='dashboard')),
    url(r'^api/v1/notification/', include('habitat.notification.urls', namespace='notification')),
    url(r'^api/v1/sensor/', include('habitat.sensors.urls', namespace='sensor')),
    url(r'^api/v1/timezone/', include('habitat.timezone.urls', namespace='timezone')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'^api/v1/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/', get_schema_view(title='HabitatOS API v1', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])),
    url(r'^api/$', RedirectView.as_view(permanent=False, url='/api/v1/')),
]

urlpatterns += [
    url(r'^grappelli/', include('grappelli.urls'), name='grappelli'),
    url(r'^', admin.site.urls, name='admin'),
]
