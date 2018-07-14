__author__ = 'wangqc'

'''
4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
'''


class Solution:
    # find an index i in short array that i-1 is less than median while i is larger that median
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        imin, imax = 0, m
        while imin <= imax:
            i = (imin + imax) >> 1
            j = ((m + n + 1) >> 1) - i
            if i > 0 and nums1[i-1] > nums2[j]: imax = i - 1
            elif i < m and nums1[i] < nums2[j-1]: imin = i + 1
            else:
                if i == 0: max_left = nums2[j-1]
                elif j == 0: max_left = nums1[i-1]
                else: max_left = max(nums1[i-1], nums2[j-1])
                if (m + n) & 1: return max_left
                if i == m: min_right = nums2[j]
                elif j == n: min_right = nums1[i]
                else: min_right = min(nums1[i], nums2[j])
                return (max_left + min_right) / 2


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.findMedianSortedArrays([1, 2], [3, 4])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))