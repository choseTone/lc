__author__ = 'wangqc'

'''
326. Power of Three

Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 3:
Input: 9
Output: true

Example 4:
Input: 45
Output: false

Follow up:
Could you do it without using any loop / recursion?
'''

import math

class Solution:
    def isPowerOfThree_loop(self, n):
        if n <= 0: return False
        while n > 1:
            if n % 3: return False
            n //= 3
        return True

    def isPowerOfThree_max_power(self, n):
        if n <= 0: return False
        max_power = 3 ** 19
        return not max_power % n

    # not a safe method log, a floating point operation, might lose accuracy
    def isPowerOfThree_log(self, n):
        if n <= 0: return False
        log3n = math.log(n, 3)
        return log3n


if __name__ == '__main__':
    from time import time

    sol = Solution()
    n = 3 ** 18
    t0 = time()
    ans0 = sol.isPowerOfThree_loop(n)
    t1 = time()
    ans1 = sol.isPowerOfThree_loop(n)
    t2 = time()
    ans2 = sol.isPowerOfThree_max_power(n)
    t3 = time()
    ans3 = sol.isPowerOfThree_log(n)
    t4 = time()
    print('ans1: %s\ntime: %.3fms' % (ans1, ((t2 - t1)) * 1000))
    print('ans2: %s\ntime: %.3fms' % (ans2, ((t3 - t2)) * 1000))
    print('ans3: %s\ntime: %.3fms' % (ans3, ((t4 - t3)) * 1000))
