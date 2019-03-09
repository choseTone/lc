__author__ = 'wangqc'

from time import time

'''
494. Target Sum

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
'''

class Solution:
    def findTargetSumWays(self, nums, S):
        # S = A - B, A is the sum of all positive elements and B is that of the negative, sum of nums + S = 2A
        # so use dp to find solution that the sum of selected positive elements is A or (sum of nums + S) / 2
        sum_nums = sum(nums)
        if S > sum_nums or (sum_nums + S) & 1: return 0
        pos = (sum(nums) + S) >> 1
        dp = [1] + [0] * pos
        for n in nums:
            for i in range(pos, n-1, -1):
                dp[i] += dp[i - n]
        return dp[pos]

if __name__ == '__main__':
    from random import randint
    sol = Solution()
    nums, S = [randint(1, 100) for _ in range(20)], randint(1, 100)
    t = time()
    ans = sol.findTargetSumWays(nums, S)
    # nums: [19, 28, 77, 71, 33, 88, 83, 58, 59, 90, 28, 1, 53, 85, 22, 15, 37, 27, 21, 91] S: 50 ans: 3146
    print('input:\nnums: %s\tS: %d\nans: %s\ntime: %.3fms' % (nums, S, ans, ((time() - t)) * 1000))