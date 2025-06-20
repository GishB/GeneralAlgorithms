"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:

    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters if it is non-empty.

"""

from typing import List

def longestCommonPrefix(strs: List[str]) -> str: # noqa
    """ Function to find the longest prefix.

    Notes:
        1. Complexity is O(N) in average. The worst case might be O(N^2)!
        2. limitations has been defined on the top of the function.
        3. Valid only for strs which content str size are not larger than 200!

    Returns:
        str of the longest prefix over all possible strs.
    """
    min_len: int = 200  # declare maximum which is expected
    min_str: str = ""  # declare default output if None strs. Here as well we will save result.

    if not strs:
        return min_str

    # Find minimum str in the strs
    for txt in strs:
        current_len = len(txt)
        if current_len <= min_len:
            min_str = txt
            min_len = current_len

    # Check that all str in strs have the same prefix.
    for txt in strs:
        # In case we have reached min_len limitation we break the loop earlier!
        if min_len <= 0:
            break

        # Current prefix for str depends on min_len
        tmp_str = txt[:min_len]

        if tmp_str != min_str:
            # If prefix for selected str are not the same for tmp str prefix we create loop and init a counter which is equal to min_len.
            counter = min_len
            while counter >= 0:
                # Check what prefix size are equal for tmp str prefix.
                condition = min_str[:counter] == txt[:counter]
                if condition:
                    # Update min_len and min_str when prefixes are valid for each str.
                    min_str = min_str[:counter]
                    min_len = counter
                    # break the loop because the condition success!
                    break
                # If checker for selected min_len failed than we update the counter.
                counter -= 1
    return min_str

if __name__ == "__main__":
    inputs = ["flower","flow","flight"]
    output = "fl"
    res = longestCommonPrefix(strs=inputs)
    if res == output:
        print("It is ok!")




