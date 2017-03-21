from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin


urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
]
