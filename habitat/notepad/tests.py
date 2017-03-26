from django.test import TestCase
from habitat.tests import HttpTest

from habitat.notepad.models import DiaryEntry


HttpTest().test_status_ok(urls=[
    '/notepad/diaryentry/',
])


class DiaryTest(TestCase):
    def setUp(self):
        DiaryEntry.objects.create(title='Test Title', content='This is the content')

    def test_slug(self):
        entry = DiaryEntry.objects.get(title='Test Title')
        self.assertEqual(entry.slug, 'the-title')
