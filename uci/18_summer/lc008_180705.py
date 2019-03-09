__author__ = 'wangqc'

'''
8. String to Integer (atoi)

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is 
found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical 
digits as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number, which are ignored and have no 
effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists 
because either str is empty or it contains only whitespace characters, no conversion is performed.
If no valid conversion could be performed, a zero value is returned.

Note:
Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: 
[−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1) or 
INT_MIN (−2^31) is returned.

Example 1:
Input: "42"
Output: 42

Example 2:
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
             
Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
             
Example 5:
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Therefore INT_MIN (−2^31) is returned.
'''


class Solution:
    # ord(i) python string decode: +, -, 0-9: 43, 45, 48-57
    def myAtoi(self, str):
        str, int_max, int_min = str.lstrip() + '$', 2 ** 31 - 1, -2 ** 31
        ans = ord((str[0])) - 48
        if ans > 10 or ans < -6 or ans in {-1, -2, -4}:
            return 0
        # str[0] in '+-'
        if ans in {-3, -5}:
            sign, ans = -4 - ans, 0
        else:
            sign = 1
        for c in str[1:]:
            digit = ord(c) - 48
            if int_min <= ans <= int_max and 0 <= digit <= 9:
                ans = ans * 10 + digit
            else:
                return min(max(ans * sign, int_min), int_max)


if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.myAtoi('  -91283472332 with word')
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))