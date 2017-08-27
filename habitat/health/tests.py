from habitat.tests import Test


class HealthTest(Test):
    assert_http_200 = [
        '/health/',

        '/health/bloodpressure/',
        '/health/bloodpressure/add/',

        '/health/disease/',
        '/health/disease/add/',

        '/health/pulseoxymetry/',
        '/health/pulseoxymetry/add/',

        '/health/stool/',
        '/health/stool/add/',

        '/health/temperature/',
        '/health/temperature/add/',

        '/health/urine/',
        '/health/urine/add/',

        '/health/weight/',
        '/health/weight/add/',
    ]
