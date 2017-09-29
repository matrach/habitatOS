#!/usr/bin/env python3

import datetime
import sqlite3
import sys
import logging
import warnings
from habitatos_client import HabitatOSBasicAuth as HabitatOS


warnings.warn('Push package to PyPI')
sys.path.append('..')


logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime).19s] %(levelname)s %(message)s')

habitatos = HabitatOS(
    url='http://localhost:8000',
    username='_api.sensors.zwave',
    password='HabitatOS_API123')


with sqlite3.connect('../sensors-data.sqlite3') as db:
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    sql = 'SELECT * FROM sensor_data WHERE sync_datetime IS NULL'

    for row in cursor.execute(sql):
        data = {
            'datetime': row['datetime'],
            'device': row['device'],
            'type': row['type'],
            'value': row['value'],
            'unit': row['unit']}

        response = habitatos.post('/sensor/zwave/', data=data)

        now = datetime.datetime.now(datetime.timezone.utc)
        dt = row['datetime']

        if response.status_code == 201:
            logging.info(f'ADD: {data}')
            with db:
                db.execute(f'UPDATE sensor_data SET sync_datetime="{now}" WHERE datetime="{dt}"')

        elif response.status_code == 200:
            logging.warning(f'UPDATE: {data}')
            with db:
                db.execute(f'UPDATE sensor_data SET sync_datetime="{now}" WHERE datetime="{dt}"')

        else:
            logging.error(f'ERROR: {data}')
