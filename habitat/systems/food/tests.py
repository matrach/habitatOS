from habitat.tests import Test


class FoodTest(Test):
    assert_http_200 = [
        '/food/',
        '/food/product/add/',
    ]
