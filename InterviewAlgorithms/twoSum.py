# Task name: Two Sum
# url: https://leetcode.com/problems/two-sum/description/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    out = []
    for indx, val in enumerate(nums):
        diff = target - val
        hashmap_key = hashmap.get(val)
        if hashmap_key:
            out = [hashmap_key[0], indx]
            break
        else:
            hashmap[diff] = [indx, val]
    return out

if __name__ == "__main__":
    print(twoSum(nums=[3,2,4], target=6))

