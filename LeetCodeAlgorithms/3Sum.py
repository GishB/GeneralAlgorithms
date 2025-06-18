"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Examples:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    """ Find all pairs which follow the rule.

    Notes:
        1. Two pointer solution;
        2. Based on sorting nums inplace.

    Args:
        nums: unsorted list of values

    Returns:
        a list of pairs list.
    """
    if len(nums) < 3:
        return []
    elif len(nums) == 3 and sum(nums) == 0:
        return [nums]

    nums.sort()
    length = len(nums)
    result = []

    for i in range(length - 2): # always minus two based on given task and two pointer solution.
        if i> 0 and nums[i] == nums[i -1]: # skip index if it is not unique from the past one
            continue

        left = i + 1 # left pointer
        right = length - 1 # right pointer


        while left < right:
            total = nums[i] + nums[left] + nums[right] # condition for the task

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                # add pairs to the result
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    # skip index if it is not unique from the past one
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    # skip index if it is not unique from the past one
                    right -= 1
                left += 1
                right -= 1
    return result

if __name__ == "__main__":
    input = [-1,0,1,2,-1,-4]
    output = [[-1,-1,2],[-1,0,1]]
    if threeSum(nums=input) == output:
        print("it is ok!")

