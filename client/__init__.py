import os
import http.client
import logging


OAUTH2_CLIENT_ID = 'EWpl5dLj4rpRFQZR6EUB9pdjdoKVOlaTHBP5SJ72'
OAUTH2_CLIENT_SECRET = 'mQVgEwTVMDa8xBgjtBsdaWcUzfDniV3hc36sX2p4hGTYOGkm6wbWTiZjfCUn7w0kmj9CHigewc60WkjPLgU4CSXPfwXpypAFIkx6CKlEzOATL3MnNtao6RXIsRjo9rjR'

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
log = logging.getLogger('habitatos_client')


class HabitatOSAbstractBaseClass:

    def __init__(self, url, username, password, debug=False):
        self.url = url
        self.username = username
        self.password = password
        self.debug = debug
        self._connection = None
        self._auth = None

    def _authenticate(self):
        raise NotImplementedError

    def _connect(self):
        raise NotImplementedError

    def _get_auth(self):
        if not self._auth:
            self._auth = self._authenticate()
        return self._auth

    def _get_connection(self):
        if not self._connection:
            self._connection = self._connect()
        return self._connection

    def _debug(self, data):
        if self.debug:
            log.debug('\n\n')
            http.client.HTTPConnection.debuglevel = 1
            log.debug(f'{data}\n\n')

    def _request(self, method='GET', path='/', data={}, headers={'Content-Type': 'application/json'}):
        url = f'{self.url}/api/v1{path}'
        auth = self._get_auth()
        connection = self._get_connection()
        self._debug(locals())
        return connection.request(method=method, url=url, data=data, headers=headers, auth=auth)

    def post(self, path='/', data={}, headers={}):
        return self._request('POST', path=path, data=data, headers={})

    def get(self, path='/', data={}, headers={}):
        return self._request('GET', path=path, data=data, headers={})

    def put(self, path='/', data={}, headers={}):
        return self._request('PUT', path=path, data=data, headers={})

    def head(self, path='/', data={}, headers={}):
        return self._request('HEAD', path=path, data=data, headers={})

    def delete(self, path='/', data={}, headers={}):
        return self._request('DELETE', path=path, data=data, headers={})


from .basic import HabitatOSBasicAuth
from .oauth import HabitatOSOAuth2
