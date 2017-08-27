from habitat.tests import Test


class InventoryTest(Test):
    assert_http_200 = [
        '/inventory/',

        '/inventory/edible/',
        '/inventory/edible/add/',

        '/inventory/item/',
        '/inventory/item/add/',
    ]
