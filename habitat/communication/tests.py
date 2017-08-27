from .models import DiaryEntry
from habitat.tests import Test


class CommunicationTest(Test):
    assert_http_200 = [
        '/communication/',
        '/communication/personalnote/',
        '/communication/personalnote/add/',
        '/communication/figure/',
        '/communication/figure/add/',
        '/communication/diaryentry/',
        '/communication/diaryentry/add/',
    ]

    def test_diary(self):
        DiaryEntry.objects.create(title='Test Title', author_id=1, content='This is the content')
        entry = DiaryEntry.objects.get(title='Test Title')
        self.assertEqual(entry.slug, 'test-title')
