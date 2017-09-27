import os
from django.conf import settings
from django.core.management.base import BaseCommand


PROJECT_NAME = settings.ROOT_URLCONF.split('.')[0]


HEADER = """[main]
host = https://www.transifex.com
"""

TEMPATE = """
[{project_name}.{name}]
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
            if app.startswith(PROJECT_NAME):
                project_name = PROJECT_NAME
                path = app.replace('.', '/')
                name = app.split('.')[-1]
                locale = os.path.join(path, 'locale')

                if os.path.isdir(locale):
                    self.stdout.write(TEMPATE.format(**locals()))
