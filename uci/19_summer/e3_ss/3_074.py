__author__ = 'wangqc'

# https://leetcode.com/problems/wiggle-sort-ii/


class Solution:
    def wiggleSort(self, nums):
        nums.sort()
        mid = len(nums) - 1 >> 1
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]


if __name__ == '__main__':
    sol = Solution()

    t1 = [1, 5, 1, 1, 6, 4]
    sol.wiggleSort(t1)
    print(t1)
