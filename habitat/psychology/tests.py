from habitat.tests import Test


class PsychologyTest(Test):
    assert_http_200 = [
        '/psychology/',
        '/psychology/questionnaire/',
        '/psychology/questionnaire/add/',
    ]
