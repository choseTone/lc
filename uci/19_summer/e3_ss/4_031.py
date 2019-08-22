__author__ = 'wangqc'

# https://leetcode.com/problems/next-permutation/

import bisect


class Solution:
    def nextPermutation(self, nums):
        i = len(nums) - 1
        while i and nums[i] <= nums[i - 1]:
            i -= 1
        if i:
            nums[i:] = nums[:i-1:-1]
            j = bisect.bisect(nums, nums[i-1], i)
            nums[j], nums[i-1] = nums[i-1], nums[j]
        else:
            return nums.reverse()


if __name__ == '__main__':
    sol = Solution()

    t1 = [2, 6, 1, 5, 7, 0]
    sol.nextPermutation(t1)
    print(t1)
