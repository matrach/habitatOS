from habitat.tests import Test


class GreenhouseTest(Test):
    assert_http_200 = [
        '/greenhouse/',
        '/greenhouse/experiment/',
        '/greenhouse/experiment/add/',
        '/greenhouse/plant/',
        '/greenhouse/plant/add/',
    ]
