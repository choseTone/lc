__author__ = 'wangqc'

# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/


class Solution:
    def numRollsToTarget(self, d, f, target):
        M = 10**9 + 7
        dp = [[0]*(target+1) for _ in range(d)]
        for j in range(1, min(f, target)+1):
            dp[0][j] = 1
        for i in range(1, d):
            for j in range(1, target+1):
                dp[i][j] = sum(dp[i-1][j-k] for k in range(1, min(f+1, j))) % M
        return dp[d-1][target]


if __name__ == '__main__':
    sol = Solution()

    t1 = 2, 6, 7
    print(sol.numRollsToTarget(*t1))

    t2 = 30, 30, 500,
    print(sol.numRollsToTarget(*t2))
