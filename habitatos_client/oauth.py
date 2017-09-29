import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session


class HabitatOSOAuth2:
    def __init__(self, url, username, password):
        super().__init__(url, username, password)
        self._token = None
        self._client = None

    def _get_token(self):
        if not self._token:
            self._token = requests.post(
                url=f'{self.url}/oauth2/token/',
                auth=HTTPBasicAuth(OAUTH2_CLIENT_ID, OAUTH2_CLIENT_SECRET),
                data={'grant_type': 'password', 'username': self.username, 'password': self.password},
            ).json()
        return self._token

    def _get_client(self):
        if not self._client:
            self._client = OAuth2Session(
                client_id=OAUTH2_CLIENT_ID,
                token=self._get_token(),
                scope=['/sensor'],
                auto_refresh_url=f'{self.url}/oauth2/token/')
        return self._client

    def _request(self, method='GET', path='/', data={}, headers={'Content-Type': 'application/json'}):
        return self._get_client().request(
            method=method,
            url=f'{self.url}/api/v1{path}',
            headers=headers,
            data=data)

    def post(self, path='/', data={}, headers={}):
        return self._request('POST', path=path, data=data, headers={})
