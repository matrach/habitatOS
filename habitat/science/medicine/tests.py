from habitat.tests import Test


class MedicineTest(Test):
    assert_http_200 = [
        '/medicine/',
        '/medicine/bloodpressure/',
        '/medicine/bloodpressure/add/',
        '/medicine/disease/',
        '/medicine/disease/add/',
        # '/medicine/excretion/',
        # '/medicine/excretion/add/',
        # '/medicine/intercourse/',
        # '/medicine/intercourse/add/',
        # '/medicine/intoxication/',
        # '/medicine/intoxication/add/',
        '/medicine/pulsoxymetry/',
        '/medicine/pulsoxymetry/add/',
        '/medicine/temperature/',
        '/medicine/temperature/add/',
        '/medicine/weight/',
        '/medicine/weight/add/',
    ]
