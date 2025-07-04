"""
Given a string s, partition it into unique segments according to the following procedure:

    Start building a segment beginning at index 0.
    Continue extending the current segment character by character until the current segment has not been seen before.
    Once the segment is unique, add it to your list of segments, mark it as seen, and begin a new segment from the next index.
    Repeat until you reach the end of s.

Return an array of strings segments, where segments[i] is the ith segment created.

Example 1:

Input: s = "abbccccd"
Output: ["a","b","bc","c","cc","d"]

Example 2:

Input: s = "aaaa"
Output: ["a","aa"]
"""
from typing import List

def partitionString(s: str) -> List[str]: # noqa
    set_ = set()
    dp = []

    length = len(s)
    f_ind = 0
    s_ind = f_ind + 1
    while (f_ind < length) and (s_ind < length):
        val = s[f_ind:s_ind]
        if val in set_:
            s_ind += 1
        else:
            f_ind = s_ind
            s_ind = f_ind + 1
            set_.add(val)
            dp.append(val)
    return dp

if __name__ == "__main__":
    test = partitionString(s="aaaaa")
    print("ok")

