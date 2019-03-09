__author__ = 'wangqc'

'''
268. Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:
Input: [3,0,1]
Output: 2

Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''


class Solution:
    def missingNumber_math(self, nums):
        n = len(nums)
        return (n * (n + 1) >> 1) - sum(nums)

    def missingNumber_xor(self, nums):
        ans = len(nums)
        for i, n in enumerate(nums):
            ans ^= i ^ n
        return ans


if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    ans = sol.missingNumber_xor([9,6,4,2,3,5,7,0,1])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

