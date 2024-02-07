import pytest
from KarpovCoursesAlgorithms.FindMajorElement import maj_element


@pytest.fixture
def list_of_tests():
    return ([[3, 5, 5, 1], 5],
            [[0, 1, 1, 1, 0, 0, 0, 0], 0])


def test_maj_element_0(list_of_tests):
    assert maj_element(list_of_tests[0][0]) == list_of_tests[0][1], "Unexpected behavior for maj element test №0"


def test_maj_element_1(list_of_tests):
    assert maj_element(list_of_tests[1][0]) == list_of_tests[1][1], "Unexpected behavior for maj element test №1"
