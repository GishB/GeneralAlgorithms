"""
Karpov.Courses algos task.

Task 1.

Here you have 2 sequences A and B which is separately sorted in ASC order. A and B contents only some int values.
You need to write merge function to sort A+B sequence in ASC order where limitation is O(A+B).

function name must be called "merge"
"""


def merge(a: list[int], b: list[int]) -> list[int]:
    """ Algos to sort two sequences.

    Note:
        - Complexity is O(N).

    Args:
        a: list of ASC sorted random int values.
        b: list of ASC sorted random int values.

    Return:
        merged a and b sequences in ASC order.
    """
    dp: list[int] = []
    iter_a: int = 0
    iter_b: int = 0
    counter: int = len(a) + len(b)
    while counter != 0:
        if iter_a == len(a):
            val_a: int = 16777215
        else:
            val_a = a[iter_a]
        if iter_b == len(b):
            val_b: int = 16777215
        else:
            val_b = b[iter_b]

        if val_a <= val_b:
            iter_a += 1
            dp.append(val_a)
        elif val_b < val_a:
            iter_b += 1
            dp.append(val_b)
        else:
            pass
        counter -= 1
    return dp

#
# if __name__ == "__main__":
#     for task in range(4):
#         if task == 0:
#             a = [1, 3, 5, 8]
#             b = [2, 6, 7, 13]
#             expected = [1, 2, 3, 5, 6, 7, 8, 13]
#         elif task == 1:
#             a = [-5, 0, 4, 9]
#             b = [1, 1]
#             expected = [-5, 0, 1, 1, 4, 9]
#         elif task == 2:
#             a = []
#             b = [1, 2, 3]
#             expected = [1, 2, 3]
#         else:
#             a = []
#             b = []
#             expected = []
#         out = merge(a, b)
#         if out == expected:
#             print(f'Custom test № {task} is OK')
#         else:
#             print(f'Test № {task} is fail')
