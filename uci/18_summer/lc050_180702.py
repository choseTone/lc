__author__ = 'wangqc'

import time

'''
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (x^n).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25

Note:
-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
'''

class Solution:
    def myPow(self, x, n):
        # recursive call
        if n < 0: x, n = 1 / x, -n
        return self.myPow(x, n - 1) * x if n & 1 else self.myPow(x * x, n >> 1) if n else 1



if __name__ == '__main__':
    sol = Solution()
    t = time.time()
    ans = sol.myPow(2, 10)
    print('ans: %s\ntime: %.2fms' % (ans, ((time.time() - t)) * 1000))