import requests
from requests.auth import HTTPBasicAuth
from habitatos_client import HabitatOSAbstractBaseClass


class HabitatOSBasicAuth(HabitatOSAbstractBaseClass):
    def _authenticate(self):
        return HTTPBasicAuth(username=self.username, password=self.password)

    def _connect(self):
        return requests.Session()