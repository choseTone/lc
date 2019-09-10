__author__ = 'wangqc'

# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/


class Solution:
    def maxSubArrayLen(self, nums, k):
        agg = max_len = 0
        prev = {}
        for i in range(len(nums)):
            agg += nums[i]
            prev.setdefault(agg, i)
            if agg == k:
                max_len = i+1
            elif agg-k in prev:
                max_len = max(max_len, i - prev[agg-k])
        return max_len


if __name__ == '__main__':
    sol = Solution()

    t1 = [1, -1, 5, -2, 3], 3,
    print(sol.maxSubArrayLen(*t1))

    t2 = [-2, -1, 2, 1], 1,
    print(sol.maxSubArrayLen(*t2))
