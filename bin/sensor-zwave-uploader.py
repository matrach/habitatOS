#!/usr/bin/env python3

import datetime
import sqlite3
import sys


import warnings
warnings.warn('Push package to PyPI')
sys.path.append('../client/')
from habitatos_client import HabitatOSBasicAuth as HabitatOS


habitatos = HabitatOS(
    url='http://localhost:8000',
    username='_api.sensors.zwave',
    password='HabitatOS_API123')


with sqlite3.connect('../sensors-data.sqlite3') as db:
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    sql = 'SELECT * FROM sensor_data WHERE sync_datetime IS NULL'

    for row in cursor.execute(sql):
        response = habitatos.post('/sensor/z-wave/', data={
            'datetime': row['datetime'],
            'device': row['device'],
            'type': row['type'],
            'value': row['value'],
            'unit': row['unit'],
        })

        if response.status_code == 200:
            now = datetime.datetime.now(datetime.timezone.utc)
            dt = row['datetime']
            print(f'UPDATE sensor_data SET sync_date="{now}" WHERE datetime="{dt}"')
            print(response.json())
            # db.execute(f'UPDATE sensor_data SET sync_date="{now}" WHERE datetime="{dt}"')
