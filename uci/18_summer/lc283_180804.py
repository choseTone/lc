__author__ = 'wangqc'

'''
283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the 
non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''


class Solution:
    def moveZeroes(self, nums):
        slow = 0
        for fast, n in enumerate(nums):
            if n:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1




if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    nums = [0,1,0,3,12]
    sol.moveZeroes(nums)
    print('ans: %s\ntime: %.3fms' % (nums, ((time() - t)) * 1000))
