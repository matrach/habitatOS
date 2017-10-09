from habitat.tests import Test


class TimezoneTest(Test):
    assert_http_200 = [
        '/api/v1/timezone/martian-standard-time/',
        '/api/v1/timezone/lunar-standard-time/',
        '/api/v1/timezone/martian-standard-time/converter/',
    ]
