from django.conf.urls import url

from habitat.drag_and_drop.views import AjaxPhotoUploadView
from habitat.drag_and_drop.views import AlbumCreateView


urlpatterns = [
    url(regex=r'^(?P<pk>\d+)/ajax-upload/$',
        view=AjaxPhotoUploadView.as_view(),
        name='ajax_photo_upload_view'),

    url(regex=r'alb/(?P<pk>\d+)/$$',
        view=AlbumCreateView.as_view(),
        name='album_view'),
]
