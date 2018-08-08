__author__ = 'wangqc'

'''
556. Next Greater Element III

Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits 
existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:
Input: 12
Output: 21

Example 2:
Input: 21
Output: -1
'''

import bisect

class Solution:
    def nextGreaterElement(self, n):
        if n < 10: return -1
        nums = [int(x) for x in str(n)]
        i = len(nums) - 1
        while nums[i] <= nums[i-1]:
            i -= 1
            if not i: return -1
        nums = nums[:i] + nums[i:][::-1]
        j = bisect.bisect(nums, nums[i-1], i)
        nums[i-1], nums[j] = nums[j], nums[i-1]
        ans = 0
        for n in nums:
            ans = ans * 10 + n
            if ans > 2 ** 31 - 1: return -1
        return ans



if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.nextGreaterElement(15293)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
