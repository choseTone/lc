__author__ = 'wangqc'

'''
219. Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such 
that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        cache = {}
        for i, n in enumerate(nums):
            if n in cache and i - cache[n] <= k:
                return True
            cache[n] = i
        return False


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.containsNearbyDuplicate([1,2,3,1], 3)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
