__author__ = 'wangqc'

'''
349. Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Note:
Each element in the result must be unique.
The result can be in any order.
'''


class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    ans = sol.intersection([4,9,5], [9,4,9,8,4])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

