from habitat.tests import Test


class ReportingTest(Test):
    assert_http_200 = [
        '/reporting/',

        '/reporting/communication/',
        '/reporting/communication/add/',

        '/reporting/incident/',
        '/reporting/incident/add/',

        '/reporting/mood/',
        '/reporting/mood/add/',

        '/reporting/repair/',
        '/reporting/repair/add/',

        '/reporting/sleep/',
        '/reporting/sleep/add/',

        '/reporting/waste/',
        '/reporting/waste/add/',
    ]
