# https://leetcode.com/problems/merge-sorted-array/
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.

from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
        Do not return anything, modify nums1 in-place instead.
    """
    p1 = m - 1
    p2 = n - 1
    p = m+n -1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p1], nums1[p] = nums1[p], nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    while p2 >= 0 and p>=0:
        nums1[p] = nums2[p2]
        p -= 1
        p2 -= 1

if __name__ == "__main__":
    merge(nums1=[4,5,6,0,0,0], m=3, nums2=[1,2,3], n=3)
    print("STOP")