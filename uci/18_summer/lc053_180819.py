__author__ = 'wangqc'

'''
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''


class Solution:
    def maxSubArray(self, nums):
        ans = curr = nums[0]
        for num in nums[1:]:
            curr = max(num, num + curr)
            ans = max(ans, curr)
        return ans


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
