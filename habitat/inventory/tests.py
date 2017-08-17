from habitat.tests import Test


class InventoryTest(Test):
    assert_http_200 = [
        '/inventory/',

        # '/inventory/consumable/',
        # '/inventory/consumable/add/',

        '/inventory/edible/',
        '/inventory/edible/add/',

        '/inventory/item/',
        '/inventory/item/add/',
    ]
