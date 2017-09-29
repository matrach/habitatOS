import os
from django.conf import settings
from django.core.management import base
from django.core.management import call_command


PROJECT_NAME = settings.ROOT_URLCONF.split('.')[0]
TRANSIFEX_USERNAME = 'astrotech'


class Command(base.BaseCommand):
    help = 'Makemessages for each app in project'

    def handle(self, *args, **options):
        self.stdout.write('Generating localized messages')
        self.stdout.write('Please run this from your terminal')

        for app in settings.INSTALLED_APPS:
            if app.startswith(PROJECT_NAME):
                path = app.replace('.', '/')
                locale = os.path.join(path, 'locale')

                if os.path.isdir(locale):
                    # call_command('')
                    self.stdout.write(f'cd {path} && django-admin makemessages -l pl -l en && cd -')

        self.stdout.write('tx push -s')
        self.stdout.write(f'open https://www.transifex.com/{TRANSIFEX_USERNAME}/{PROJECT_NAME}/translate/#pl')
        self.stdout.write('tx pull')
        self.stdout.write('python manage.py compilemessages')
