__author__ = 'wangqc'


# https://leetcode.com/problems/burst-balloons/

class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        dp, N = {}, len(nums)
        for i in range(N-2, -1, -1):
            for j in range(i+1, N):
                dp[i,j] = max((dp[i,k]+dp[k,j]+nums[i]*nums[k]*nums[j]
                               for k in range(i+1,j)), default=0)
        return dp[0, N-1]


if __name__ == '__main__':
    sol = Solution()

    t1 = [3,1,5,8],
    print(sol.maxCoins(*t1))
