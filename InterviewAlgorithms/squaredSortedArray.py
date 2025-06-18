from typing import List

def sortedSquares(nums: List[int]) -> List[int]:
    nums2 = [val ** 2 for val in nums if val < 0]
    nums1 = [val ** 2 for val in nums if val >= 0]

    length2 = len(nums2) - 1
    length1 = len(nums1) - 1

    p1, p2 = 0, 0

    result = []
    while p1 <= length1 and p2 <= length2:
        if nums1[p1] <= nums2[p2]:
            result.append(nums1[p1])
            p1 += 1
        elif nums1[p1] > nums2[p2]:
            result.append(nums2[p2])
            p2 += 1
    return result

if __name__ == "__main__":
    print(sortedSquares(nums=[-4,-1,0,3,10]))