from habitat.tests import Test


class InventoryTest(Test):
    assert_http_200 = [
        '/medicine/',
        '/medicine/bloodpressure/',
        '/medicine/bloodpressure/add/',
        '/medicine/disease/',
        '/medicine/disease/add/',
        '/medicine/evaluation/',
        '/medicine/evaluation/add/',
        '/medicine/excretion/',
        '/medicine/excretion/add/',
        '/medicine/intercourse/',
        '/medicine/intercourse/add/',
        '/medicine/intoxication/',
        '/medicine/intoxication/add/',
        '/medicine/meal/',
        '/medicine/meal/add/',
        '/medicine/pulsoxymetry/',
        '/medicine/pulsoxymetry/add/',
        '/medicine/qualityoflife/',
        '/medicine/qualityoflife/add/',
        '/medicine/sleep/',
        '/medicine/sleep/add/',
        '/medicine/temperature/',
        '/medicine/temperature/add/',
        '/medicine/weight/',
        '/medicine/weight/add/',
    ]
