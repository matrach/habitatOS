import logging
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from habitat.notepad.models import DiaryEntry

log = logging.getLogger(__name__)


class HttpTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser('testrunner', 'test@test.com', 'testrunner')
        self.admin = Client()
        self.admin.login(username='testrunner', password='testrunner')

    def tearDown(self):
        self.admin.logout()
        self.user.delete()

    def test_diary(self):
        DiaryEntry.objects.create(title='Test Title', author_id=1, content='This is the content')
        entry = DiaryEntry.objects.get(title='Test Title')
        self.assertEqual(entry.slug, 'test-title')

    def test_url(self):
        urls = [
            '/notepad/',
            '/notepad/personalnote/',
            '/notepad/figure/',
            '/notepad/diaryentry/',
        ]

        for url in urls:
            response = self.admin.get(url)
            log.info("%s, %s" % (response.status_code, url))
            self.assertEqual(response.status_code, 200)

