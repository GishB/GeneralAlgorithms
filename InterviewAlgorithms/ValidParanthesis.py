#  Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.


def isValid(s: str) -> bool:
    by_default = True
    cache = []
    left_dict = {"(": ")", "[": "]", "{": "}"}
    right_dict = {")": "(", "]": "[", "}": "{"}
    for index, bracket in enumerate(s):
        if cache:
            tmp_bracket = left_dict.get(bracket)
            if not tmp_bracket:
                if cache[-1] == right_dict.get(bracket):
                    cache.pop()
            else:
                cache.append(bracket)
        else:
            cache.append(bracket)
    return by_default if not cache else False

if __name__ == "__main__":
    print(isValid(s="{{()}}"))
