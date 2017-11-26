#!/usr/bin/env python3

import json
import datetime
import logging
import sqlite3
import serial


DATABASE = '/home/pi/database/sensor-data.sqlite3'
ALLOWED_PARAMETERS = ['air_temperature', 'air_humidity', 'water_temperature', 'luminosity', 'power_k1', 'power_k2', 'power_k3', 'power_k4']
DEVICE = '/dev/ttyACM0'


logging.basicConfig(
    format='[%(asctime).19s] %(levelname)s %(message)s',
    level=logging.INFO
)


with sqlite3.connect(DATABASE) as db:
    db.execute("""CREATE TABLE IF NOT EXISTS sensor_data (
        datetime DATETIME PRIMARY KEY,
        sync_datetime DATETIME DEFAULT NULL,
        device VARCHAR(255),
        parameter VARCHAR(255),
        value VARCHAR(255),
        unit VARCHAR(255));""")
    db.execute('CREATE UNIQUE INDEX IF NOT EXISTS sensor_data_datetime_index ON sensor_data (datetime);')
    db.execute('CREATE INDEX IF NOT EXISTS sensor_data_sync_datetime_index ON sensor_data (sync_datetime);')


def save_to_sqlite3(data):
    for parameter, value in data.items():

        if not parameter or parameter not in ALLOWED_PARAMETERS:
            continue

        with sqlite3.connect(DATABASE) as db:
            db.execute('INSERT INTO sensor_data VALUES (:datetime, NULL, :device, :parameter, :value, :unit)', {
                'datetime': datetime.datetime.now(datetime.timezone.utc),
                'parameter': parameter,
                'value': value,
                'unit': '',
                'device': 'hydroponics',
            })


if __name__ == '__main__':
    with serial.Serial(port=DEVICE, baudrate=115200) as ser:
        while True:
            line = ser.readline()
            try:
                data = json.loads(line)
                save_to_sqlite3(data)
                logging.info(data)
            except json.decoder.JSONDecodeError:
                logging.error(line)

