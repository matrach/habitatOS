from habitat.tests import Test


class BuildingTest(Test):
    fixtures = [
        'module.json',
        'storage.json',
    ]

    assert_http_200 = [
        '/building/',
        '/building/module/',
        '/building/module/add/',
        '/building/module/1/change/',
        '/building/storage/',
        '/building/storage/add/',
        '/building/storage/1/change/',

        '/api/v1/building/lightning/test/',
    ]
