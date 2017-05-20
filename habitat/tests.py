import logging
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client


class Test(TestCase):
    assert_http_200 = []

    def setUp(self):
        self.logger = logging.getLogger(__name__)
        self.user = User.objects.create_superuser('testrunner', 'test@test.com', 'testrunner')
        self.client.login(username='testrunner', password='testrunner')

    def tearDown(self):
        self.client.logout()
        self.user.delete()

    def test_http_200(self):
        for url in self.assert_http_200:
            response = self.client.get(url)

            if response.status_code != 200:
                self.logger.error(f'{response.status_code} {url}')
                raise AssertionError(f'HTTP {response.status_code} for "{url}"')
            else:
                self.logger.info(f'{response.status_code} {url}')
