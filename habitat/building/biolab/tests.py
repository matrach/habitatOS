from habitat.tests import Test


class GreenhouseTest(Test):
    assert_http_200 = [
        '/biolab/',
        '/biolab/experiment/',
        '/biolab/experiment/add/',
        '/biolab/plant/',
        '/biolab/plant/add/',
    ]
