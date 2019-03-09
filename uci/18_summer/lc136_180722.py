__author__ = 'wangqc'

'''
136. Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
'''


class Solution:
    # constant space solution: bit manipulation
    def singleNumber(self, nums):
        ans = 0
        for n in nums:
            ans ^= n
        return ans


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.singleNumber([4, 1, 2, 1, 2])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
