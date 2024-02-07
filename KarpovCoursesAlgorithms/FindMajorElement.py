"""
Task № 3.

You have a list "nums" which is len(n)

Let`s called an element as majority if count of the element in the list are > n // 2.

It is guaranteed that you will always have a majority element in all given lists.

You need to write function "maj_element(nums)" which will return the major element.

For example:
    1.
        nums = [3, 5, 5, 1]
        return 5
    2.
        nums = [0, 1, 1, 1, 0, 0, 0, 0]
        return 0
"""


def maj_element(nums: list[int]) -> int:
    """ Function to find major element in the list.

    Note:
        - Expected that list always contents major element.
        - Complexity is O(N).

    Arg:
        nums: a list of elements.

    Return:
        The major element from the list.
    """
    len_list: int = len(nums)
    dict_nums: dict = {}
    counter: int = 0
    while counter != len_list:
        val_temp = nums[counter]
        is_saved = dict_nums.get(val_temp, False)
        if is_saved:
            dict_nums[val_temp] = dict_nums[val_temp] + 1
        else:
            dict_nums[val_temp] = 1
        counter += 1
    major_element = 0
    for number in dict_nums.keys():
        val = dict_nums[number]
        if val >= len_list // 2:
            major_element = number
            break
    return major_element