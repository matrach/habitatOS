#!/usr/bin/env python3

import os
import datetime
import sqlite3
import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session


os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

DATABASE = '../sensors-data.sqlite3'

API_USERNAME = '_api.sensors.zwave'
API_PASSWORD = 'HabitatOS_API123'

OAUTH2_CLIENT_ID = 'EWpl5dLj4rpRFQZR6EUB9pdjdoKVOlaTHBP5SJ72'
OAUTH2_CLIENT_SECRET = 'mQVgEwTVMDa8xBgjtBsdaWcUzfDniV3hc36sX2p4hGTYOGkm6wbWTiZjfCUn7w0kmj9CHigewc60WkjPLgU4CSXPfwXpypAFIkx6CKlEzOATL3MnNtao6RXIsRjo9rjR'


class HabitatOS:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self._token = None
        self._client = None

    @property
    def token(self):
        if not self._token:
            self._token = requests.post(
                url=f'{self.url}/oauth2/token/',
                auth=HTTPBasicAuth(OAUTH2_CLIENT_ID, OAUTH2_CLIENT_SECRET),
                data={'grant_type': 'password', 'username': API_USERNAME, 'password': API_PASSWORD},
            ).json()
        return self._token

    @property
    def client(self):
        if not self._client:
            self._client = OAuth2Session(
                client_id=OAUTH2_CLIENT_ID,
                token=self.token,
                scope=['/sensor'],
                auto_refresh_url=f'{self.url}/oauth2/token/')
        return self._client

    def _request(self, method='GET', path='/', data={}, headers={'Content-Type': 'application/json'}):
        return self.client.request(
            method=method,
            url=f'{self.url}/api/v1{path}',
            headers=headers,
            data=data)

    def post(self, path='/', data={}, headers={}):
        return self._request('POST', path=path, data=data, headers={})


habitatos = HabitatOS(
    url='http://localhost:8000',
    username='_api.sensors.zwave',
    password='HabitatOS_API123')


with sqlite3.connect(DATABASE) as db:
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    sql = 'SELECT * FROM sensor_data WHERE sync_datetime IS NULL'

    for row in cursor.execute(sql):
        response = habitatos.post('/sensor/z-wave/', data={
            'datetime': row['datetime'],
            'type': row['type'],
            'value': row['value'],
            'unit': row['unit'],
            'device': row['device'],
        })

        if response.status_code == 200:
            now = datetime.datetime.now(datetime.timezone.utc)
            dt = row['datetime']
            print(f'UPDATE sensor_data SET sync_date="{now}" WHERE datetime="{dt}"')
            # db.execute(f'UPDATE sensor_data SET sync_date="{now}" WHERE datetime="{dt}"')
