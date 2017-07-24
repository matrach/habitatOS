from habitat.tests import Test


class InventoryTest(Test):
    assert_http_200 = [
        '/reporting/',
        '/reporting/mood/',
        '/reporting/mood/add/',
        '/reporting/sleep/',
        '/reporting/sleep/add/',
    ]
