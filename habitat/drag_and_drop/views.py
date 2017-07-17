from django.views.generic import View, TemplateView, CreateView, UpdateView

from braces.views import AjaxResponseMixin
from braces.views import JSONResponseMixin
from braces.views import LoginRequiredMixin
from braces.views import SuperuserRequiredMixin

from .models import Album
from .models import Photo


class AjaxPhotoUploadView(LoginRequiredMixin, SuperuserRequiredMixin, JSONResponseMixin, AjaxResponseMixin, View):

    def post_ajax(self, request, *args, **kwargs):
        try:
            album = Album.objects.get(pk=kwargs.get('pk'))
        except Album.DoesNotExist:
            return self.render_json_response(
                context_dict={'message': 'Album not found.'},
                status=404)

        Photo.objects.create(
            album=album,
            file=request.FILES['file'])

        return self.render_json_response(
            context_dict={'message': 'File uploaded successfully!'},
            status=200)


class AlbumCreateView(CreateView):
    model = Album
    template_name = 'drag-and-drop/photo_list.html'
    fields = '__all__'
