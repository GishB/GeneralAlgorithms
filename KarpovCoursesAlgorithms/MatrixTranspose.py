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


def transpose(array: list[list[float | int]]) -> list[list[float | int]]:
    matrix_length = len(array)
    L = list(chain(*array))
    new_matrix = []
    for i in range(matrix_length):
        new_matrix.append([L[i::matrix_length]])
    return new_matrix


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    out = transpose(matrix)
    test = 0
