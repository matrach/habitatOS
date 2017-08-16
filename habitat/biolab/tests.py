from habitat.tests import Test


class BiolabTest(Test):
    assert_http_200 = [
        '/biolab/',

        '/biolab/experiment/',
        '/biolab/experiment/add/',

        '/biolab/observation/',
        '/biolab/observation/add/',

        '/biolab/plant/',
        '/biolab/plant/add/',
    ]
