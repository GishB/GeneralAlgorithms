# You are given a sorted unique integer array nums.
#
# A range [a,b] is the set of all integers from a to b (inclusive).
#
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
#
# Each range [a,b] in the list should be output as:
# "a->b" if a != b
# "a" if a == b

# Example 1:
#
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
#
# Example 2:
#
# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
#

from typing import List

def summaryRanges(nums: List[int]) -> List[str]:
    if nums:
        dp = []
        length_num = len(nums)
        a_val = nums[0]
        for index, current_val in enumerate(nums):
            if index > length_num - 1:
                break
            else:
                next_val = nums[index+1] if index != length_num -1 else nums[index]
                b_val = current_val
                if current_val + 1 != next_val:
                    if a_val != b_val:
                        dp.append(f"{a_val}->{b_val}")
                    else:
                        dp.append(f"{a_val}")
                    a_val = next_val
        return dp
    else:
        return nums

if __name__ == "__main__":
    print(summaryRanges(nums=[1,2,3,5,6,9]))

