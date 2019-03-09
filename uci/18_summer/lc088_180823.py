__author__ = 'wangqc'

'''
88. Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]
'''

class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m + n - 1
        while m and n:
            if nums1[m-1] > nums2[n-1]:
                nums1[i] = nums1[m-1]
                m -= 1
            else:
                nums1[i] = nums2[n-1]
                n -= 1
            i -= 1
        nums1[:n] = nums2[:n]


if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    nums1, nums2 = [1,2,3,0,0,0], [2,5,6]
    sol.merge(nums1, 3, nums2, 3)
    print('ans: %s\ntime: %.3fms' % (nums1, ((time() - t)) * 1000))

