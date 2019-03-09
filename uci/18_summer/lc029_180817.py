__author__ = 'wangqc'

'''
29. Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3

Example 2:
Input: dividend = 7, divisor = -3
Output: -2

Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: 
[−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
'''


class Solution:
    def divide(self, dividend, divisor):
        ans, sign = 0, [1, -1][(dividend < 0) is (divisor > 0)]
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            shift = 0
            while dividend >= divisor << shift:
                shift += 1
            ans, dividend = ans + (1 << shift - 1), dividend - (divisor << shift - 1)
        return min(max(-2**31, ans * sign), 2**31 - 1)


if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    ans = sol.divide(10, 3)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

