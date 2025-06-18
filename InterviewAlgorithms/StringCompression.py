# https://leetcode.com/problems/string-compression/description/

# Given an array of characters chars, compress it using the following algorithm:
#
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
#
#     If the group's length is 1, append the character to s.
#     Otherwise, append the character followed by the group's length.
#
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
#
# After you are done modifying the input array, return the new length of the array.
#
# You must write an algorithm that uses only constant extra space.

from typing import List

def compress(chars: List[str]) -> int:
    if len(chars) == 1:
        return len(chars)
    p1, p2 = 0, 1
    length = len(chars) - 1
    compressed_list = []
    count_tmp_char = 1
    while p2 <= length:
        if chars[p1] == chars[p2]:
            count_tmp_char += 1
            if p2 == length:
                compressed_list.append(chars[p1])
                compressed_list.append(str(count_tmp_char))
        elif chars[p1] != chars[p2]:
            if count_tmp_char == 1:
                compressed_list.append(chars[p1])
            else:
                compressed_list.append(chars[p1])
                compressed_list.append(str(count_tmp_char))
            count_tmp_char = 1
        p1 += 1
        p2 += 1
    return len(compressed_list)

if __name__ == "__main__":
    print(compress(["a", "a", "b", "b"]))

