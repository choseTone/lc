__author__ = 'wangqc'

'''
300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n^2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
'''


class Solution:
    # keep update dp[i+1] with n in dp where dp[i] < n < dp[i+1].
    # len(dp) indicates the size of the longest subsequence has been made so far
    def lengthOfLIS(self, nums):
        dp = []
        for n in nums:
            l, r = 0, len(dp)
            while l != r:
                m = (l + r) >> 1
                if dp[m] < n: l = m + 1
                else: r = m
            if l == len(dp): dp.append(n)
            else: dp[l] = n
        return len(dp)


if __name__ == '__main__':
    from time import time
    from random import randint

    sol = Solution()
    t = time()
    nums = [randint(1, 20) for _ in range(20)]
    ans = sol.lengthOfLIS(nums)
    print('nums: %s\nans: %s\ntime: %.3fms' % (nums, ans, ((time() - t)) * 1000))
