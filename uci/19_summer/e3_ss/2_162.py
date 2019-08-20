__author__ = 'wangqc'

# https://leetcode.com/problems/find-peak-element/


class Solution:
    def findPeakElement(self, nums):
        l, r = 0, len(nums)-1
        while l < r:
            m = l + r >> 1
            if nums[m] > nums[m+1]:
                r = m
            else:
                l = m + 1
        return l


if __name__ == '__main__':
    sol = Solution()

    t1 = [1,2,1,3,5,6,4],
    print(sol.findPeakElement(*t1))
