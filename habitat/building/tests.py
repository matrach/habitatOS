from habitat.tests import Test


class BuildingTest(Test):
    fixtures = [
        'building.module.json',
        'building.storage.json',
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
