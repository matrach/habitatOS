from habitat.tests import Test


class healthTest(Test):
    assert_http_200 = [
        '/health/',
        '/health/bloodpressure/',
        '/health/bloodpressure/add/',
        '/health/disease/',
        '/health/disease/add/',
        # '/health/excretion/',
        # '/health/excretion/add/',
        # '/health/intercourse/',
        # '/health/intercourse/add/',
        # '/health/intoxication/',
        # '/health/intoxication/add/',
        '/health/pulsoxymetry/',
        '/health/pulsoxymetry/add/',
        '/health/temperature/',
        '/health/temperature/add/',
        '/health/weight/',
        '/health/weight/add/',
    ]
