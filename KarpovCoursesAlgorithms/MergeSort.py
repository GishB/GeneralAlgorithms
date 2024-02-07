"""
Task 6.

Write MergeSort function.

Baseline idea is:
    - If len(arr) <= 1 return arr
    - If len(arr) > 1 split array //2 and apply merge_sort and then merge two sorted sequences.

Function should be called "merge_sort()". In: arr | Out: Sorted arr.

"""


def merge_sort(arr: list[int]) -> list[int]:
    """ Sort array in ASC order.

    Note:
        - Complexity is O(Nlog(N)).
        - This is a recursive algorithm implementation.

    Arg:
        arr: an array of ing values.

    Return:
        Sorted array in ASC order.
    """
    len_arr = len(arr)
    if len_arr <= 1:
        return arr
    else:
        arr_a = merge_sort(arr[:len_arr // 2])
        arr_b = merge_sort(arr[len_arr // 2:])
        return merge(arr_a, arr_b)


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

