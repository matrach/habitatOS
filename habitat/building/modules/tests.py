from habitat.tests import Test


class ModulesTest(Test):
    assert_http_200 = [
        '/modules/',
        '/modules/module/',
        '/modules/module/add/',
    ]
