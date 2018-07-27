__author__ = 'wangqc'

'''
162. Find Peak Element

A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.

Note:
Your solution should be in logarithmic complexity.
'''


class Solution:
    # log complexity
    def findPeakElement(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            m1 = (l + r) >> 1
            m2 = m1 + 1
            if nums[m1] < nums[m2]: l = m2
            else: r = m1
        return l

    def findPeakElementLinear(self, nums):
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return i - 1
        return len(nums) - 1


if __name__ == '__main__':
    from time import time
    from numpy import random

    sol = Solution()
    # nums = random.choice(10**10, 10**10, replace=False)
    nums = list(range(10**6))
    t0 = time()
    ans = sol.findPeakElement(nums)
    t1 = time()
    ans1 = sol.findPeakElement(nums)
    t2 = time()
    ans2 = sol.findPeakElementLinear(nums)
    t3 = time()

    # sol1 0.004ms; sol2 88.538ms;
    print('ans1: %s\ntime: %.3fms' % (ans1, ((t2 - t1)) * 1000))
    print('ans2: %s\ntime: %.3fms' % (ans2, ((t3 - t2)) * 1000))
