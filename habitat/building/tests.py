from habitat.tests import Test


class BuildingTest(Test):
    assert_http_200 = [
        '/building/',
        '/building/module/',
        '/building/module/add/',
        '/building/lightning/test/',
    ]
