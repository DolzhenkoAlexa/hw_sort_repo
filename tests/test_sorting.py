import pytest
from sorting_algorithms import bubble_sort, heap_sort, merge_sort, quick_sort

test_cases = [
    ([], []),
    ([0], [0]),
    ([0, 0, 0], [0, 0, 0]),
    ([0, 1, 2, 3], [0, 1, 2, 3]),
    ([1, 0, 2, 3, 1], [0, 1, 1, 2, 3]),
    ([90, 30, 5, -90000, 2, -100, 1000], [-90000, -100, 2, 5, 30, 90, 1000]),
]

@pytest.mark.parametrize("arr_before_sort,expected", test_cases)
def test_bubble_sort(arr_before_sort, expected):
    assert bubble_sort(arr_before_sort) == expected

@pytest.mark.parametrize("arr_before_sort,expected", test_cases)
def test_heap_sort(arr_before_sort, expected):
    assert heap_sort(arr_before_sort) == expected

@pytest.mark.parametrize("arr_before_sort,expected", test_cases)
def test_merge_sort(arr_before_sort, expected):
    assert merge_sort(arr_before_sort) == expected

@pytest.mark.parametrize("arr_before_sort,expected", test_cases)
def test_quick_sort(arr_before_sort, expected):
    assert quick_sort(arr_before_sort) == expected