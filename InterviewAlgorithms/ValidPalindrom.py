# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true

# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
# Constraints:
#
#     1 <= s.length <= 2 * 105
#     s consists only of printable ASCII characters.

def isPalindrome(s: str) -> bool:
    condition = True
    s = s.lower().strip()
    s = [letter for letter in s if letter.isalnum()]
    if s == 1:
        return condition
    else:
        index_left = 0
        index_right = len(s) - 1
        while index_left < index_right and condition:
            condition = s[index_left] == s[index_right]
            if condition:
                index_left += 1
                index_right -= 1
            else:
                break
        return condition

if __name__ == "__main__":
    print(isPalindrome("ab!#ba"))

