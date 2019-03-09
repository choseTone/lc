__author__ = 'wangqc'

'''
217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if 
every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

class Solution:
    def containsDuplicate(self, nums):
        record = set()
        for n in nums:
            if n in record: return True
            record.add(n)
        return False


if __name__ == '__main__':
    from time import time
    from random import randint

    sol = Solution()
    nums = [randint(1, 50) for _ in range(10)]

    t = time()
    ans = sol.containsDuplicate(nums)
    print('nums: %s\nans: %s\ntime: %.3fms' % (nums, ans, ((time() - t)) * 1000))

