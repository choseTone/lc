__author__ = 'wangqc'

'''
523. Continuous Subarray Sum

Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous 
subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

'''

class Solution:
    def checkSubarraySum(self, nums, k):
        n = len(nums)
        if n < 2: return False
        presum, record = 0, {0: -1}
        for i in range(n):
            presum += nums[i]
            if k: presum %= k
            if presum in record:
                if i - record[presum] > 1:
                    return True
            else: record[presum] = i
        return False


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.checkSubarraySum([23, 2, 6, 4, 7], 6)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
