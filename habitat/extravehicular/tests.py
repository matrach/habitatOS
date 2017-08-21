from habitat.tests import Test


class ExtravehucularTest(Test):
    assert_http_200 = [
        '/extravehicular/',

        '/extravehicular/activity/',
        '/extravehicular/activity/add/',

        '/extravehicular/contingency/',
        '/extravehicular/contingency/add/',

        '/extravehicular/location/',
        '/extravehicular/location/add/',

        '/extravehicular/objective/',
        '/extravehicular/objective/add/',

        '/extravehicular/report/',
        '/extravehicular/report/add/',

        '/extravehicular/spacewalker/',
        '/extravehicular/spacewalker/add/',
    ]
