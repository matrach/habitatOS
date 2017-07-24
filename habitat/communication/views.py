from django.views.generic import TemplateView

from .models import DiaryEntry


class Diary(TemplateView):
    template_name = 'communication/diary-entry.html'

    def get_context_data(self, slug, **kwargs):
        entry = DiaryEntry.objects.get(slug=slug)
        return {'entry': entry}
