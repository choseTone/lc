__author__ = 'wangqc'

'''
27. Remove Element

Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,1,2,2,3,0,4,2], val = 2,
Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
Note that the order of those five elements can be arbitrary.
It doesn't matter what values are set beyond the returned length.
'''


class Solution:
    def removeElement(self, nums, val):
        i, j = 0, len(nums)
        while i < j:
            if nums[i] != val:
                i += 1
            else:
                nums[i] = nums[j-1]
                j -= 1
        return i


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.removeElement([0,1,2,2,3,0,4,2], 2)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
