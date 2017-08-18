from habitat.tests import Test


class WaterTest(Test):
    assert_http_200 = [
        '/water/',

        '/water/drinkingwater/',
        '/water/drinkingwater/add/',

        '/water/greenwater/',
        '/water/greenwater/add/',

        '/water/technicalwater/',
        '/water/technicalwater/add/',
    ]
