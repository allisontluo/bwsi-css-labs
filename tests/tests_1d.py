from labs.lab_1.lab_1d import two_sum


def test_two_sum_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_two_sum_with_negatives():
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]


def test_two_sum_with_duplicates():
    assert two_sum([3, 3], 6) == [0, 1]


def test_two_sum_later_pair():
    assert two_sum([1, 2, 3, 4, 6], 10) == [3, 4]


def test_two_sum_no_solution_fallback():
    assert two_sum([1, 2, 3], 100) == []