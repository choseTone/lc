__author__ = 'wangqc'

# https://leetcode.com/problems/predict-the-winner/


class Solution:
    def PredictTheWinner(self, nums):
        N = len(nums)
        dp = [0] * N
        for l in range(N-2, -1, -1):
            for r in range(l+1, N):
                dp[r] = max(nums[l]-dp[r], nums[r]-dp[r-1])
        return dp[N-1] >= 0



if __name__ == '__main__':
    sol = Solution()

    t1 = [1,5,2],
    print(sol.PredictTheWinner(*t1))

    t2 = [1,5,233,7],
    print(sol.PredictTheWinner(*t2))