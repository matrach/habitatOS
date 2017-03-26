from habitat.tests import Test


class InventoryTest(Test):
    assert_http_200 = [
        '/inventory/',
        '/inventory/food/',
        '/inventory/food/add/',
        '/inventory/item/',
        '/inventory/item/add/',
    ]
