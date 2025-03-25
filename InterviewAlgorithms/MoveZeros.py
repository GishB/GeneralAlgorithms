# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.

# Example 1:
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Example 2:
#
# Input: nums = [0]
# Output: [0]

from typing import List

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    first_ind = 0
    second_ind = first_ind + 1
    while second_ind < length:
        left_val = nums[first_ind]
        right_val = nums[second_ind]
        # обновляем оба индекса так как их значения не нулевые.
        if (left_val != 0 and right_val != 0) or (left_val !=0 and right_val == 0):
            first_ind += 1
            second_ind += 1
        # обновляем только правый индекс.
        elif left_val == 0 and right_val == 0:
            second_ind += 1
        # swap values
        else:
            nums[first_ind], nums[second_ind] = nums[second_ind], nums[first_ind]
    print(nums)


if __name__ == "__main__":
    # https: // leetcode.com / problems / move - zeroes / description /
    moveZeroes([0,1,0,3,12])