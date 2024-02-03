""" Karpov.Courses

Task 9.

In this task we will implement QuickSelect algorithm.

You have an array and an int k. You need to find the k largest element in the array without any sort algos.

Your task is to write "kth_largest(array, k)" which requires:
    In: array of int and an int k
        Out: the k largest element from the array.
"""
import random
from typing import Optional


def kth_largest(array: list[int], k: int) -> Optional[int]:
    """ QuickSelect algorithm to find the k largest element in the array.

    Note:
        - Complexity in average case is O(N).
        - This is a recursive algorithm implementation.

    Args:
        array: list of int values.
        k: the k largest number in the array.

    Return:
        Value of the k largest element.
    """
    if array is not None:
        pivot_index = random.randint(0, len(array)-1)
        pivot = array[pivot_index]
    else:
        return array
    left_partition = [val for val in array if val < pivot]
    right_partiion = [val for val in array if val >= pivot]
    count_equals = len([val for val in right_partiion if val == pivot])
    if count_equals == len(right_partiion) and k < count_equals:
        return pivot
    if len(right_partiion) == k:
        return pivot
    elif len(right_partiion) >= k:
        return kth_largest(right_partiion, k)
    else:
        return kth_largest(left_partition, k-len(right_partiion))


if __name__ == "__main__":
    for test_num in range(7):
        k = 2
        if test_num == 0:
            test_array = [8, 0, 1, 4, 3, 6, 4, 2, 7]
            expected = 7
        elif test_num == 1:
            test_array = [-1, 1, 3, 5, 7]
            expected = 5
        elif test_num == 2:
            test_array = [-10, -50, 700, 500, 999, 1005, 3005]
            expected = 1005
        elif test_num == 3:
            test_array = [5, -1, 1, 5]
            expected = 5
        elif test_num == 4:
            test_array = [0, 0, 0]
            expected = 0
        elif test_num == 5:
            test_array = [3, 2, 1, 5, 6, 4]
            expected = 5
        else:
            test_array = [3, 2, 3, 1, 2, 4, 5, 5, 6]
            expected = 4
            k = 4
        out = kth_largest(test_array, k)
        if out == expected:
            print("OK")
        else:
            print("Failed")
