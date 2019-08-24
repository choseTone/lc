__author__ = 'wangqc'


# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        M, N = len(nums1), len(nums2)
        if M > N:
            M, N, nums1, nums2 = N, M, nums2, nums1
        lo, hi = 0, M
        while lo <= hi:
            i = lo + hi >> 1
            j = (M + N + 1 >> 1) - i
            if i > 0 and nums1[i-1] > nums2[j]:
                hi = i - 1
            elif i < M and nums1[i] < nums2[j-1]:
                lo = i + 1
            else:
                left = max(nums1[i-1], nums2[j-1]) if i*j else nums2[j-1] if j else nums1[i-1]
                if M + N & 1:
                    return left / 1.
                right = nums2[j] if i==M else nums1[i] if j==N else min(nums1[i], nums2[j])
                return (left + right) / 2.


if __name__ == '__main__':
    sol = Solution()

    t1 = [1,3],[2],
    print(sol.findMedianSortedArrays(*t1))

    t2 = [1,2],[3,4],
    print(sol.findMedianSortedArrays(*t2))
