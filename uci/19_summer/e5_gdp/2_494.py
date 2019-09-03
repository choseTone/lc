__author__ = 'wangqc'

# https://leetcode.com/problems/target-sum/


class Solution:
    def findTargetSumWays(self, nums, S):
        s = sum(nums)
        if s < S or (s + S) & 1:
            return 0
        T = (s + S) >> 1
        dp = [1] + [0] * T
        for x in nums:
            for t in range(T, x-1, -1):
                dp[t] += dp[t-x]
        return dp[T]


if __name__ == '__main__':
    sol = Solution()

    t1 = [1, 1, 1, 1, 1], 3,
    print(sol.findTargetSumWays(*t1))