import pytest
from KarpovCoursesAlgorithms.QuickSelect import kth_largest


@pytest.fixture
def list_of_tests():
    return (
        [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4],
        [[0, 0, 0], 0, 2],
        [[-10, -50, 700, 500, 999, 1005, 3005], 1005, 2]
    )


def test_kth_largest_0(list_of_tests):
    assert kth_largest(array=list_of_tests[0][0], k=list_of_tests[0][2]) == list_of_tests[0][1], \
        "Unexpected the largest element for kth_largest test №0"


def test_kth_largest_1(list_of_tests):
    assert kth_largest(array=list_of_tests[1][0], k=list_of_tests[1][2]) == list_of_tests[1][1], \
        "Unexpected the largest element for kth_largest test zero №1"


def test_kth_largest_2(list_of_tests):
    assert kth_largest(array=list_of_tests[1][0], k=list_of_tests[1][2]) == list_of_tests[1][1], \
        "Unexpected the largest element for kth_largest test zero №1"
