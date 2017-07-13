from habitat.tests import Test


class FoodTest(Test):
    assert_http_200 = [
        '/food/',
        '/food/product/',
        '/food/product/add/',
        '/food/tag/',
        '/food/tag/add/',
        '/food/unit/',
        '/food/unit/add/',
        '/food/diet/',
        '/food/diet/add/',
        '/food/meal/',
        '/food/meal/add/',
    ]
