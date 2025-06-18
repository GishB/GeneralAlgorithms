# Longest Substring Without Repeating Characters

# Desc: Given a string s, find the length of the longest without duplicate characters.
# Example:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "dvdf"
# Output: 3
# Explanation: vdf is the longest!

# Try to implement pointer solution

def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    max_len = 0
    left = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
    return max_len

if __name__ == "__main__":
    test_out = lengthOfLongestSubstring(s="vdvef")
    print(test_out)