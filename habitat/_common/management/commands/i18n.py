from django.conf import settings
from django.core.management.base import BaseCommand


SKIP = [
    'habitat._common',
    'habitat.dashboard',
]


class Command(BaseCommand):
    help = 'Makemessages for app'

    def handle(self, *args, **options):
        self.stdout.write('Generating localized messages')

        for app in settings.INSTALLED_APPS:
            if app.startswith('habitat') and app not in SKIP:
                path = app.replace('.', '/')
                self.stdout.write(path)
