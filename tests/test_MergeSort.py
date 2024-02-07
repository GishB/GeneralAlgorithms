import pytest
from KarpovCoursesAlgorithms.MergeSort import merge, merge_sort


@pytest.fixture
def list_of_tests():
    return ([[3, 1, 2, -1, -5, 10, -50, -100, 9], [-100, -50, -5, -1, 1, 2, 3, 9, 10]],
            [[1, 2, 3, 9, 10], [-100, -50, -5, -1], [-100, -50, -5, -1, 1, 2, 3, 9, 10]])


def test_merge_sort(list_of_tests):
    assert merge_sort(list_of_tests[0][0]) == list_of_tests[0][1], "Unexpected behavior for simple test merge_sort"


def test_merge(list_of_tests):
    assert merge(list_of_tests[1][0], list_of_tests[1][1]) == list_of_tests[1][
        2], "Unexpected behavior for simple test merge"
