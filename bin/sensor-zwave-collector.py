#!/usr/bin/env python3

import datetime
import logging
import signal
import sqlite3
import libopenzwave


DATABASE = '/home/pi/lunares_hab/sensors-data.sqlite3'
ALLOWED_MEASUREMENTS = ['Battery Level', 'Powerlevel', 'Temperature', 'Luminance', 'Relative Humidity', 'Ultraviolet']  # 'Burglar'
device = '/dev/ttyACM0'
log = 'Info'
sniff = 60.0


options = libopenzwave.PyOptions(
    config_path='/usr/local/etc/openzwave/',
    user_path='/home/pi/lunares_hab/',
    cmd_line='--logging false')

options.lock()
manager = libopenzwave.PyManager()
manager.create()


with sqlite3.connect(DATABASE) as db:
    db.execute("""CREATE TABLE IF NOT EXISTS sensor_data (
        datetime DATETIME PRIMARY KEY,
        sync_datetime DATETIME DEFAULT NULL,
        device VARCHAR(255),
        type VARCHAR(255),
        value VARCHAR(255),
        unit VARCHAR(255));""")
    db.execute('CREATE UNIQUE INDEX IF NOT EXISTS sensor_data_datetime_index ON sensor_data (datetime);')
    db.execute('CREATE UNIQUE INDEX IF NOT EXISTS sensor_data_sync_datetime_index ON sensor_data (sync_datetime);')


def save_to_sqlite3(args):
    values = args.get('valueId')

    if not values or values.get('label') not in ALLOWED_MEASUREMENTS:
        return None

    with sqlite3.connect(DATABASE) as db:
        db.execute('INSERT INTO sensor_data VALUES (:datetime, NULL, :device, :type, :value, :unit)', {
            'datetime': datetime.datetime.now(datetime.timezone.utc),
            'type': values.get('label'),
            'value': values.get('value'),
            'unit': values.get('units'),
            'device': '{base:08x}-{node}'.format(
                base=values.get('homeId'),
                node=values.get('nodeId'))})


if __name__ == '__main__':
    logging.info('Add watcher')
    manager.addWatcher(save_to_sqlite3)

    logging.info('Add device')
    manager.addDriver(device)

    try:
        signal.pause()

    finally:
        logging.info('Remove watcher')
        manager.removeWatcher(save_to_sqlite3)

        logging.info('Remove device')
        manager.removeDriver(device)
