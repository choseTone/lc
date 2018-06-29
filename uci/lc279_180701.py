__author__ = 'wangqc'

import time

'''
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
    # update a dp list, for each round check all possible combinations of squares (1 square with length i
    # and the smallest number of the rest squares has been calculated and stored in dp[-i*i]) and find the smallest
    # dp[-i*i] and plus extra 1 (square with length i)
    def numSquares(self, n):
        dp = [0]
        while n >= len(dp):
            dp.append(min(dp[-i*i] for i in range(1, int(len(dp)**0.5)+1)) + 1)
        return dp[n]


if __name__ == '__main__':
    sol = Solution()
    t = time.time()
    ans = sol.numSquares(1292)
    print('ans: %d\ntime: %.2fms' % (ans, ((time.time()-t))*1000))