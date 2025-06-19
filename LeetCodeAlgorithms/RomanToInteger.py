"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.


Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""
roman_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def romanToInt(s: str) -> int: # noqa
    """ This function convert valid roman int to modern int.

    Notes:
        1. This function used cache to store tmp info.
        2. Average complexity is O(N), but in the worst case it is going to be O(N^2).

    Args:
        s: string representation of valid roman values.

    Returns:
        modern int representation of value.
    """
    cache_roman = []
    integer = 0
    c_ind = 0
    length = len(s)

    while c_ind < length:
        current_roman = s[c_ind]

        if len(cache_roman) == 0:  # если ничего нет, то обновляем информацию
            cache_roman.append(current_roman)
        else:
            past_val = roman_dict.get(cache_roman[0])
            current_val = roman_dict.get(current_roman)
            if cache_roman[-1] != current_roman and past_val > current_val:
                for ind in range(len(cache_roman)):
                    cache_roman.pop(-1)
                    integer += past_val
                cache_roman.append(current_roman)
            elif cache_roman[-1] != current_roman and past_val < current_val:
                cache_roman.pop(-1)
                new_val = current_val - past_val
                integer += new_val
            else:
                cache_roman.append(current_roman)

        c_ind += 1

    if len(cache_roman) != 0:
        for ind in range(len(cache_roman)):
            val = cache_roman.pop(-1)
            integer += roman_dict.get(val)
    return integer

if __name__ == "__main__":
    input = "MCMXCIV" # noqa
    output = 1994
    if romanToInt(input) == output:
        print("It is ok!")