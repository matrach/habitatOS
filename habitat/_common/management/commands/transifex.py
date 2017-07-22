from django.apps import apps
from django.conf import settings
from django.core.management.base import BaseCommand

HEADER = """[main]
host = https://www.transifex.com

[habitatos.main]
file_filter = habitat/locale/<lang>/LC_MESSAGES/django.po
source_file = habitat/locale/en/LC_MESSAGES/django.po
source_lang = en
type = PO
"""

TEMPATE = """
[habitatos.{name}]
file_filter = {path}/locale/<lang>/LC_MESSAGES/django.po
source_file = {path}/locale/en/LC_MESSAGES/django.po
source_lang = en
type = PO
"""


class Command(BaseCommand):
    help = 'Generates transifex config'

    def handle(self, *args, **options):
        self.stdout.write(HEADER)

        for app in settings.INSTALLED_APPS:
            if app.startswith('habitat'):
                path = app.replace('.', '/')
                name = app.split('.')[-1]
                self.stdout.write(TEMPATE.format(**locals()))
