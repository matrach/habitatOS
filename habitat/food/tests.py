from habitat.tests import Test


class FoodTest(Test):
    assert_http_200 = [
        '/food/',
        '/food/diet/',
        '/food/diet/add/',
        '/food/meal/',
        '/food/meal/add/',
        '/food/dayplan/',
        '/food/dayplan/add/',
        '/food/product/',
        '/food/product/add/',
    ]
