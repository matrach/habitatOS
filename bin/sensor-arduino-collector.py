#!/usr/bin/env python3

import json
import datetime
import logging
import sqlite3
import serial


logging.basicConfig(
    format='[%(asctime).19s] %(levelname)s %(message)s',
    level=logging.INFO
)


DATABASE = '/home/pi/database/sensor-data.sqlite3'
DEVICE = '/dev/ttyACM0'
MEASUREMENTS = {
    'air_temperature': 'C',
    'air_humidity': '%',
    'water_temperature': 'C',
    'luminosity': 'lux',
    'power_k1': 'on/off',
    'power_k2': 'on/off',
    'power_k3': 'on/off',
    'power_k4': 'on/off',
}


with sqlite3.connect(DATABASE) as db:
    db.execute("""CREATE TABLE IF NOT EXISTS sensor_data (
        datetime DATETIME PRIMARY KEY,
        sync_datetime DATETIME DEFAULT NULL,
        device VARCHAR(255),
        parameter VARCHAR(255),
        value REAL,
        unit VARCHAR(255));""")
    db.execute('CREATE UNIQUE INDEX IF NOT EXISTS sensor_data_datetime_index ON sensor_data (datetime);')
    db.execute('CREATE INDEX IF NOT EXISTS sensor_data_sync_datetime_index ON sensor_data (sync_datetime);')


def save_to_sqlite3(data):
    for parameter, value in data.items():
        unit = MEASUREMENTS.get(parameter, None)

        with sqlite3.connect(DATABASE) as db:
            db.execute('INSERT INTO sensor_data VALUES (:datetime, NULL, :device, :parameter, :value, :unit)', {
                'datetime': datetime.datetime.now(datetime.timezone.utc),
                'parameter': parameter,
                'value': float(value),
                'unit': unit,
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
