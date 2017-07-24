from .models import DiaryEntry
from habitat.tests import Test


class NotepadTest(Test):
    assert_http_200 = [
        '/communication/',
        '/communication/personalnote/',
        '/communication/personalnote/add/',
        '/communication/figure/',
        '/communication/figure/add/',
        '/communication/diaryentry/',
        '/communication/diaryentry/add/',
        # '/static/communication/js/tinymce.js',
        # '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
    ]

    def test_diary(self):
        DiaryEntry.objects.create(title='Test Title', author_id=1, content='This is the content')
        entry = DiaryEntry.objects.get(title='Test Title')
        self.assertEqual(entry.slug, 'test-title')
