__author__ = 'wangqc'

# https://leetcode.com/problems/partition-equal-subset-sum/


class Solution:
    # 480 ms
    def canPartitionDP(self, nums):
        S, N = sum(nums), len(nums)
        if S & 1:
            return False
        T = S >> 1
        dp = [True] + [False]*T
        for x in nums:
            for s in range(x, T+1)[::-1]:
                dp[s] |= dp[s-x]
            if dp[T]:
                return True
        return False

    # 48 ms, works way better then sum(nums) is large
    def canPartitionDFS(self, nums):
        S, N, memo = sum(nums), len(nums), {0: True}
        if S & 1:
            return False
        nums.sort(reverse=True)

        def dfs(i, x):
            if x not in memo:
                memo[x] = False
                for j in range(i, N):
                    if x >= nums[j] and dfs(j+1, x-nums[j]):
                        memo[x] = True
                        break
            return memo[x]

        return dfs(0, S>>1)


if __name__ == '__main__':
    sol = Solution()

    t1 = [1,5,11,5],
    print(sol.canPartitionDP(*t1))
    print(sol.canPartitionDFS(*t1))

    t2 = [1,2,3,5],
    print(sol.canPartitionDP(*t2))
    print(sol.canPartitionDFS(*t2))