import requests
from requests.auth import HTTPBasicAuth
from . import HabitatOSAbstractBaseClass


class HabitatOSBasicAuth(HabitatOSAbstractBaseClass):
    def _authenticate(self):
        return HTTPBasicAuth(username=self.username, password=self.password)

    def _connect(self):
        return requests.Session()
