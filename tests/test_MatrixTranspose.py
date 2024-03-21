import pytest
import numpy as np
from numpy.linalg import det
from InterviewAlgorithms.MatrixTranspose import transpose


@pytest.fixture
def list_of_tests():
    """ Two matrices.
    """
    return ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[1, 2], [3, 4]])


def test_MatrixTranspose(list_of_tests):
    """ Check that determinant are equal for transposed matrices.

    Arg:
        list of matrices for tests.
    """
    test_a = np.array(transpose(list_of_tests[0]))
    test_b = np.array(transpose(list_of_tests[1]))
    assert det(test_a) == det(np.array(list_of_tests[0]).T), "numpy says that determinant is different for 3x3 matrix!"
    assert det(test_b) == det(np.array(list_of_tests[1]).T), "numpy says that determinant is different for 2x2 matrix!"


