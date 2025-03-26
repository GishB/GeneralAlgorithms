# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times
# as it shows in both arrays and you may return the result in any order.

from typing import List

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    length1 = len(nums1)
    length2 = len(nums2)
    intersection = []

    if length1 < length2:
        nums1, nums2 = nums2, nums1

    dict_of_values = dict()

    for val in nums2:
        if dict_of_values.get(val):
            dict_of_values[val] += 1
        else:
            dict_of_values[val] = 1

    for val in nums1:
        if dict_of_values.get(val):
            counter_tmp = dict_of_values.get(val)
            if counter_tmp > 0:
                intersection.append(val)
                dict_of_values[val] -= 1

    return intersection

if __name__ == "__main__":
    print(intersect(nums1=[1,2,3,4,3,4,3], nums2=[3,4,3]))