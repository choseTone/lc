__author__ = 'wangqc'

'''
209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of 
which the sum ≥ s. If there isn't one, return 0 instead.

Example: 
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2

Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
'''


class Solution:
    def minSubArrayLen(self, s, nums):
        cur_sum, n, l = 0, len(nums), 0
        ans = n + 1
        for i in range(n):
            cur_sum += nums[i]
            while cur_sum >= s:
                ans = min(ans, i - l + 1)
                cur_sum, l = cur_sum - nums[l], l + 1
        return ans - n - 1 and ans



if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.minSubArrayLen(7, [2,3,1,2,4,3])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
