# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]

# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3),
# while the positions of other numbers are changed (for example, 1 and 5).

# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.

# sorted([1,3,4])

# comp complexity O(N*log(N))
# mem complexity O(N)

def merge(left_sequence: list, right_sequence: list) -> list:
    merged_list = []
    p0, p1 = 0, 0
    length_l = len(left_sequence)
    length_r = len(right_sequence)
    while (p0 < length_l) and (p1 < length_r):
        if left_sequence[p0] > right_sequence[p1]:
            merged_list.append(right_sequence[p1])
            p1 += 1
        else:
            merged_list.append(left_sequence[p0])
            p0 += 1

    while p0 < length_l:
        merged_list.append(left_sequence[p0])
        p0 += 1

    while p1 < length_r:
        merged_list.append(right_sequence[p1])
        p1 += 1
    return merged_list


# [1], [2] - > [1, 2]

# [1, 2], [0, 3] - > [0, 1, 2, 3]

def sort(nums: list) -> list:
    if len(nums) <= 1:
        return nums
    else:
        index = len(nums) // 2

        left_array = sort(nums[:index])
        right_array = sort(nums[index:])

        return merge(left_array, right_array)


if __name__ == "__main__":
    print(sort(nums=[1,0,3,2]))