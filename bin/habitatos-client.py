#!/usr/bin/env python3

import http.client
import json
import logging


DATA = [{'notificationType': 'ValueChanged', 'homeId': 3241427042, 'nodeId': 2, 'valueId': {'homeId': 3241427042, 'type': 'Decimal', 'value': 22.399999618530273, 'genre': 'User', 'id': 72057594076479506, 'units': 'C', 'nodeId': 2, 'readOnly': True, 'index': 1, 'label': 'Temperature', 'instance': 1, 'commandClass': 'COMMAND_CLASS_SENSOR_MULTILEVEL'}}]


conn = http.client.HTTPConnection('localhost', 8000)


for data in DATA:
    data = data['valueId']

    if data['units'] == 'C':
        units = 'Celsius'
    else:
        units = 'Fahrenheit'

    conn.request('PUT', url='/sensor/data/', body=json.dumps({
        'device_id': f'{data["homeId"]}-{data["nodeId"]}',
        'type': data['type'],
        'value': data['value'],
        'message_id': data['id'],
        'units': units,
    }))

response = conn.getresponse()

if response.status != 201:
    logging.error(f'{response.status}: {response.reason}')

