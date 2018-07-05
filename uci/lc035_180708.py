__author__ = 'wangqc'

'''
35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it 
would be if it were inserted in order.
You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
'''


class Solution:
    def searchInsert(self, nums, target):
        l, r = 0, len(nums)
        while l != r:
            m = (l + r) >> 1
            if nums[m] < target: l = m + 1
            else: r = m
        return l



if __name__ == '__main__':
    from time import time
    from random import randint

    sol = Solution()
    t = time()
    nums = sorted(randint(1, 20) for _ in range(20))
    ans = sol.searchInsert(nums, 10)
    print('nums: %s\nans: %s\ntime: %.3fms' % (nums, ans, ((time() - t)) * 1000))