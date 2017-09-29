from habitat.tests import Test


class TimezoneTest(Test):
    assert_http_200 = [
        '/api/v1/dashboard/clock/',
    ]
