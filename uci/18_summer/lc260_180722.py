__author__ = 'wangqc'

'''
260. Single Number III

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly 
twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
'''


class Solution:
    # constant space solution: bit manipulation
    def singleNumber(self, nums):
        ab, a, b, diff = 0, 0, 0, 1
        for n in nums:
            ab ^= n
        while not (ab & diff):
            diff <<= 1
        for n in nums:
            if n & diff:
                a ^= n
            else: b ^= n
        return [a, b]

if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.singleNumber([1, 2, 1, 3, 2, 5])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
