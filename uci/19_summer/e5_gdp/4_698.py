__author__ = 'wangqc'

# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/


class Solution:
    def canPartitionKSubsets(self, nums, k):
        s = sum(nums)
        if s % k:
            return False
        N, T, dp = len(nums), s // k, [0] * k
        nums.sort(reverse=True)

        def dfs(i):
            if i == N:
                return len(set(dp)) == 1
            for j in range(k):
                dp[j] += nums[i]
                if dp[j] <= T and dfs(i+1):
                    return True
                dp[j] -= nums[i]
                if not dp[j]:
                    break
            return False

        return nums[0] <= T and dfs(0)


if __name__ == '__main__':
    sol = Solution()

    t1 = [4, 3, 2, 3, 5, 2, 1], 4,
    print(sol.canPartitionKSubsets(*t1))
