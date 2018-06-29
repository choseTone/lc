__author__ = 'wangqc'

import time

'''
264. Ugly Number II

Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:  
1 is typically treated as an ugly number.
n does not exceed 1690.
'''

class Solution:
    # compute whole nums before the function and time counter starts
    ugly_nums = sorted(2**a * 3**b * 5**c for a in range(31) for b in range(20) for c in range(14))
    def nthUglyNumber_cheat(self, n):
        return self.ugly_nums[n-1]

    # ai is the index of the smallest member that hasn't been multiplied by 2 yet in the nums, bi is for 3
    # and ci is for 5; a, b, c is the cache storing nums[ai]*2, nums[bi]*3 and nums[ci]*5 to save repeat ops
    def nthUglyNumber(self, n):
        nums = [1]
        a, b, c = 2, 3, 5
        ai = bi = ci = 1
        for _ in range(n-1):
            cur = min(a, b, c)
            nums.append(cur)
            if cur == a:
                a = nums[ai] * 2
                ai += 1
            if cur == b:
                b = nums[bi] * 3
                bi += 1
            if cur == c:
                c = nums[ci] * 5
                ci += 1
        return nums[-1]


if __name__ == '__main__':
    sol = Solution()
    t1 = time.time()
    ans1 = sol.nthUglyNumber(1690)
    t2 = time.time()
    ans2 = sol.nthUglyNumber_cheat(1690)
    print('sol1 ans: %d\ntime: %.2fms\n' % (ans1, ((t2 - t1)) * 1000))
    print('sol2 ans: %d\ntime: %.2fms' % (ans2, ((time.time() - t2)) * 1000))