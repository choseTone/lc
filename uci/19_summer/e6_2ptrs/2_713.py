__author__ = 'wangqc'

# https://leetcode.com/problems/subarray-product-less-than-k/


class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        product, i, cnt = 1, 0, 0
        for j, x in enumerate(nums):
            product *= x
            while product >= k:
                product /= nums[i]
                i += 1
            cnt += j - i + 1
        return cnt


if __name__ == '__main__':
    sol = Solution()

    t1 = [10, 5, 2, 6], 100,
    print(sol.numSubarrayProductLessThanK(*t1))

    t2 = [1, 2, 3], 0,
    print(sol.numSubarrayProductLessThanK(*t2))