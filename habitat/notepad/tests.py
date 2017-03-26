from habitat.notepad.models import DiaryEntry
from habitat.tests import Test


class NotepadTest(Test):
    assert_http_200 = [
        '/notepad/',
        '/notepad/personalnote/',
        '/notepad/personalnote/add/',
        '/notepad/figure/',
        '/notepad/figure/add/',
        '/notepad/diaryentry/',
        '/notepad/diaryentry/add/',
    ]

    def test_diary(self):
        DiaryEntry.objects.create(title='Test Title', author_id=1, content='This is the content')
        entry = DiaryEntry.objects.get(title='Test Title')
        self.assertEqual(entry.slug, 'test-title')
