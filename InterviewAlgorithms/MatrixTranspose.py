"""
Your task is to transpose given matrix without numpy implementation.

in: [[1,2,3],
    [4,5,6],
    [7,8,9]]

out: [[1,4,7],
      [2,5,8],
      [3,6,9]]

"""
from itertools import chain


def transpose(matrix: list[list[float | int]]) -> list[list[float | int]]:
    """ This function apply transpose over given matrix.

    Arg:
        matrix: list of list where all values are float or int types.

    Return:
        transposed matrix.
    """
    matrix_length = len(matrix)
    L = list(chain(*matrix))
    return [L[i::matrix_length] for i in range(matrix_length)]
