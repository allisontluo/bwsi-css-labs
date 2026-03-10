import pytest
from labs.lab_1.lab_1c import max_subarray_sum


def test_max_subarray_typical_case():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_max_subarray_single_element():
    assert max_subarray_sum([5]) == 5
    assert max_subarray_sum([-7]) == -7


def test_max_subarray_all_negative():
    assert max_subarray_sum([-8, -3, -6, -2, -5, -4]) == -2


def test_max_subarray_all_positive():
    assert max_subarray_sum([1, 2, 3, 4]) == 10


def test_max_subarray_mixed():
    assert max_subarray_sum([5, -2, 3, 4]) == 10
    assert max_subarray_sum([1, -1, 1, -1, 1]) == 1


def test_max_subarray_empty_list():
    with pytest.raises(ValueError, match="Input list cannot be empty."):
        max_subarray_sum([])