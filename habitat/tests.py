import logging
from django.conf import settings
from django.test import TestCase
from django.test.client import Client

log = logging.getLogger(__name__)


class HttpTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.client.login(
            username=settings.TEST.get('USERNAME'),
            password=settings.TEST.get('PASSWORD'))

    def test_status_ok(self, urls):
        for url in urls:
            response = self.client.get(url)
            log.info("%s, %s" % (response.status_code, url))
            self.assertEqual(response.status_code, 200)
