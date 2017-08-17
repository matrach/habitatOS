from habitat.tests import Test


class SensorsTest(Test):
    assert_http_200 = [
        '/sensors/',

        '/sensors/temperature/',
        '/sensors/temperature/add/',

        '/sensors/humidity/',
        '/sensors/humidity/add/',

        '/sensors/luminance/',
        '/sensors/luminance/add/',
    ]
