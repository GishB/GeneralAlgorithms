"""
Task 7.

You have a grid m x n filled by positive values. Find a path from the left up corner to the right down corner where
sum of positive numbers will be the lowest.

For each iteration over grid you can choose to go right or down on 1 cell.

Your task is to write function "min_path(grid)" which requires:
    In: grid (n * m)
     Out: Minimum int value (sum of values for chosen path versus all possibilities)
"""


def min_path(grid: list[list[int]]) -> int:
    """ Find minimum cost for the best path in the grid.

    Note:
        - Complexity is O(N^2) because we have to check all possibles cells in the grid.
        - Here we have greedy algorithm implementation which chose always the best way from the two past states.

    Arg:
        grid: some randomly generated grid like NxN matrix with not null filled values.

    Return:
        Value which represent minimum sum of cost for the chosen path.
    """
    m_space = len(grid)
    n_space = len(grid[0])
    mem_grid = [[0 for i in range(n_space)] for j in range(m_space)]
    for i in range(m_space):
        for j in range(n_space):
            if i == 0 and j == 0:
                mem_grid[0][0] = grid[i][j]
            elif i == 0 and j != 0:
                mem_grid[0][j] = grid[0][j] + mem_grid[0][j - 1]
            elif j == 0 and i != 0:
                mem_grid[i][0] = grid[i][0] + mem_grid[i - 1][0]
            else:
                mem_grid[i][j] = grid[i][j] + min(mem_grid[i - 1][j], mem_grid[i][j - 1])
    return mem_grid[m_space - 1][n_space - 1]


if __name__ == "__main__":
    for test_num in range(2):
        if test_num == 0:
            test_grid = [[0, 1, 2, 3, 4], [1, 12, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 17], [4, 5, 6, 7, 8]]
            min_sum = min_path(test_grid)
            expected = sum([0, 1, 2, 3, 4, 5, 6, 7, 8])
        elif test_num == 1:
            test_grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
            min_sum = min_path(test_grid)
            expected = 7

        if min_sum == expected:
            print("OK")
        else:
            print("Failed")
