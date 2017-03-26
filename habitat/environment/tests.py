from habitat.tests import Test


class EnvironmentTest(Test):
    assert_http_200 = [
        '/environment/',
        '/environment/temperature/',
        '/environment/temperature/add/',
        '/environment/humidity/',
        '/environment/humidity/add/',
        '/environment/luminosity/',
        '/environment/luminosity/add/',
    ]
