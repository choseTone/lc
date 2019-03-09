__author__ = 'wangqc'

'''
540. Single Element in a Sorted Array

Given a sorted array consisting of only integers where every element appears twice except for one element which appears 
once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
Note: Your solution should run in O(log n) time and O(1) space.
'''


class Solution:
    def singleNonDuplicate(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) >> 1
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]
            if m & 1 and nums[m] == nums[m-1] or not(m & 1) and nums[m] == nums[m+1]:
                l = m + 1
            else:
                r = m - 1
        return nums[l]


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.singleNonDuplicate([1,1,2])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
