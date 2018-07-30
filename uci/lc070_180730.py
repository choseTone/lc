__author__ = 'wangqc'

'''
70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''


class Solution(object):
    def climbStairs(self, n):
        if n == 1: return 1
        dp = [1, 2] + [0] * (n-2)
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.climbStairs(30)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
