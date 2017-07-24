import json
from django.http import HttpResponse
from django.views.generic import View, TemplateView


class NotificationServerView(View):
    def get(self, request):
        last_id = request.META.get('HTTP_LAST_EVENT_ID')
        id = 1
        data = None

        if not data:
            return HttpResponse(json.dumps(''), content_type='text/event-stream')

        assert '\n\n' not in data, 'two line breaks in a row signifies an end of message'
        return HttpResponse(json.dumps({'id': id, 'data': data}), content_type='text/event-stream')


class NotificationClientView(TemplateView):
    template_name = 'notification/frontend.html'
