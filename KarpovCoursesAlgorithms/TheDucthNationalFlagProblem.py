"""
Karpov.Courses

Task 5.

You have a list "nums" len(n) where each element represented in int values. For example,
red is 0, white is 1 and blue is 2.

You need to sort it where all elements of one color in order like
0, 1 and 2.

For this task you will need to create a function "color_sort(nums)"

Limitations:
    1. You can`t create a new list.
    2. You can`t use sorted() or something like this.
"""


def color_sort(nums: list[int]) -> list[int]:
    """ Sort three unique colors in ASC order for the given list.

    Note:
        - Complexity is O(N).

    Arg:
        nums: list of int values from 0 to 3.

    Return:
        Sorted list in ASC order.
    """
    length = len(nums)
    if length != 0:
        ind_red: int = 0
        ind_white: int = 0
        ind_blue: int = length - 1
        while ind_white <= ind_blue:
            white_val = nums[ind_white]
            if white_val == 0:
                red_val = nums[ind_red]
                nums[ind_red] = white_val
                nums[ind_white] = red_val
                ind_red += 1
                ind_white += 1
            elif white_val == 1:
                ind_white += 1
            elif white_val == 2:
                blue_val = nums[ind_blue]
                nums[ind_white] = blue_val
                nums[ind_blue] = white_val
                ind_blue -= 1
            else:
                pass
    return nums


# if __name__ == "__main__":
#     for test in range(3):
#         if test == 0:
#             nums = [2, 0, 1, 0, 2]
#             expected = [0, 0, 1, 2, 2]
#         elif test == 1:
#             nums = [2, 1, 0]
#             expected = [0, 1, 2]
#         else:
#             nums = [2, 1, 1, 0, 0, 2, 2]
#             expected = [0, 0, 1, 1, 2, 2, 2]
#
#         out = color_sort(nums)
#         if out == expected:
#             print("OK")
#         else:
#             print("Failed")
