# Окруженные острова

# Вам дан массив board размера m x n, содержащий 'X' (вода) и 'O' (остров).
# Ваша задача — затопить все острова, окруженные с четырех сторон водой
# (т.е. все 'O', окруженные с четырех сторон 'X'). Все буквы X и O английские.
# Чтобы затопить остров, нужно все его 'O' превратить в 'X'.

# Example:
# X - X - X - X - X
# X - O - O - O - X
# O - X - X - X - X

from typing import List, Optional, Set, Tuple

def bfs(board: List, x_start: int, y_start: int, visited: Set) -> Tuple[List, Set]:
    stack = [(x_start, y_start)]
    visited = visited
    up_condition, right_condition, down_condition, left_condition = False, False, False, False
    while stack:
        x_pos, y_pos = stack.pop()
        if (x_pos, y_pos) in visited:
            pass
        else:
            if board[y_pos][x_pos] == "O":
                visited.add((x_pos, y_pos))

            if (x_pos - 1 >= 0) and (board[y_pos][x_pos-1] == "X"):
                left_condition = True
            elif (x_pos - 1 >= 0) and (board[y_pos][x_pos-1] == "O") and (x_pos - 1, y_pos) not in visited:
                stack.append((x_pos - 1, y_pos))
                left_condition = False
            elif (x_pos - 1 >= 0) and (x_pos - 1, y_pos) not in visited:
                left_condition = False

            if (x_pos + 1 < len(board[0])) and (board[y_pos][x_pos + 1] == "X"):
                right_condition = True
            elif (x_pos + 1 < len(board[0])) and (board[y_pos][x_pos + 1] == "O") and (x_pos + 1, y_pos) not in visited:
                stack.append((x_pos + 1, y_pos))
                right_condition = False
            elif (x_pos + 1 < len(board[0])) and (x_pos + 1, y_pos) not in visited:
                right_condition = False

            if (y_pos + 1 < len(board)) and (board[y_pos + 1][x_pos] == "X"):
                up_condition = True
            elif (y_pos + 1 < len(board)) and (board[y_pos + 1][x_pos] == "O") and (x_pos, y_pos + 1) not in visited:
                stack.append((x_pos, y_pos + 1))
                up_condition = False
            elif (y_pos + 1 < len(board)) and (x_pos, y_pos + 1) not in visited:
                up_condition = False

            if (y_pos - 1 >= 0) and (board[y_pos - 1][x_pos] == "X"):
                down_condition = True
            elif (y_pos - 1 >= 0) and (board[y_pos - 1][x_pos] == "O") and (x_pos, y_pos - 1) not in visited:
                stack.append((x_pos, y_pos - 1))
                down_condition = False
            elif (y_pos - 1 >= 0) and (x_pos, y_pos - 1) not in visited:
                down_condition = False

    if up_condition and right_condition and down_condition and left_condition:
        while visited:
            x_pos, y_pos = visited.pop()
            board[y_pos][x_pos] = "X"
    return board, visited

def drown(board: Optional[List]) -> Optional[List]:
    if board is None:
        return board
    if board:
        visited = set()
        for y_i in range(len(board)):
            for x_i in range(len(board[0])):
                if board[y_i][x_i] != "X" and board[y_i][x_i] == "O" and (x_i, y_i) not in visited:
                    board, visited = bfs(board=board, x_start=x_i, y_start=y_i, visited=visited)
    return board

# if __name__ == "__main__":
#     example = [["X", "X", "X", "X", "X"], ["X", "O", "X", "O", "X"], ["O", "X", "X", "O", "X"]]
#     print(drown(board=example))

