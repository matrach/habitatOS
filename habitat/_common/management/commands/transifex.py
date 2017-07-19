from django.apps import apps
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Generates transifex config'

    def handle(self, *args, **options):
        for app in apps.get_models():
            print(dir(app))

            if app.label.startswith('habitat'):
                self.stdout.write(self.style.SUCCESS(f'{name}'))
