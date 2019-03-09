__author__ = 'wangqc'

import time

'''
279. Perfect Square

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

class Solution:
    # def numSquares(self, n):
    #     dp = [0]
    #     while len(dp) <= n:
    #         dp += min(dp[-i*i] for i in range(1, int(len(dp) ** 0.5) + 1)) + 1,
    #     return dp[n]

    # updated on Aug.27th
    def numSquares(self, n):
        if n < 2: return n
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        count, check = 0, {n}
        while check:
            count += 1
            next_check = set()
            for x in check:
                for y in squares:
                    if x == y: return count
                    if x < y: break
                    next_check.add(x - y)
            check = next_check
        return count


if __name__ == '__main__':
    sol = Solution()
    t = time.time()
    ans = sol.numSquares(5374)
    print('ans: %d\ntime: %.2fms' % (ans, ((time.time()-t))*1000))