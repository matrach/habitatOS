from habitat.tests import Test


class SensorsTest(Test):
    assert_http_200 = [
        '/sensors/',
        '/sensors/carbondioxide/',
        '/sensors/carbondioxide/add/',
        '/sensors/carbonmonoxide/',
        '/sensors/carbonmonoxide/add/',
        '/sensors/humidity/',
        '/sensors/humidity/add/',
        '/sensors/illuminance/',
        '/sensors/illuminance/add/',
        '/sensors/network/',
        '/sensors/network/add/',
        '/sensors/oxygen/',
        '/sensors/oxygen/add/',
        '/sensors/pressure/',
        '/sensors/pressure/add/',
        '/sensors/radiation/',
        '/sensors/radiation/add/',
        '/sensors/temperature/',
        '/sensors/temperature/add/',
        '/sensors/voltage/',
        '/sensors/voltage/add/',
        '/sensors/weather/',
        '/sensors/weather/add/',

        '/api/v1/sensor/chart/',
        '/api/v1/sensor/zwave/',
    ]
