"""
Task № 2.

You have 2 subsequences s and t. You must return True if s is in t and False otherwise.

For this task the expected subsequence s in t is string which can be created via removing some symbols. However, you
have to keep letter order in subsequence t.

For example:
    Терма and Телеграмма -> True.
"""


def is_subsequence(s: str, t: str) -> bool:
    """ Find subsequence in general sequence.

    Note:
        - Complexity is O(N) that is because we go in one directional and allocate memory with dp.

    Args:
        s: some subsequence of strings which may represent anything.
        t: general sequence which may contains subsequence.

    Return:
        True if subsequence is in general sequence or False.
    """
    dp: list[str] = []
    iter_s: int = 0
    iter_t: int = 0
    len_s: int = len(s)
    len_t: int = len(t)
    while iter_t != len_t:
        if iter_s == len_s:
            break
        val_s = s[iter_s]
        val_t = t[iter_t]
        if val_s == val_t:
            dp.append(val_s)
            iter_s += 1
            iter_t += 1
        else:
            iter_t += 1
    return "".join(dp) == s


# if __name__ == "__main__":
#     for task in range(3):
#         if task == 0:
#             s = "abd"
#             t = "aiebkgdle"
#             expected = True
#         elif task == 1:
#             s = 'Терма'
#             t = 'Телеграмма'
#             expected = True
#         elif task == 2:
#             s = "axe"
#             t = "abgirx"
#             expected = False
#
#         out = is_subsequence(s, t)
#         if out == expected:
#             print(f"Test № {task} is OK")
#         else:
#             print(f"Test № {task} failed")
