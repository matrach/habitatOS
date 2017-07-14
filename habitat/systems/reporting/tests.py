from habitat.tests import Test


class InventoryTest(Test):
    assert_http_200 = [
        '/reporting/',
        # '/reporting/report/',
        # '/reporting/report/add/',
        # '/reporting/attachment/',
        # '/reporting/attachment/add/',
    ]
