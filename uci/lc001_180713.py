__author__ = 'wangqc'

'''
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution:
    def twoSum(self, nums, target):
        cache = {}
        for i, n in enumerate(nums):
            if target - n in cache:
                return [cache[target - n], i]
            cache[n] = i


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.twoSum([2, 7, 11, 15], 9)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))