__author__ = 'wangqc'

'''
689. Maximum Sum of 3 Non-Overlapping Subarrays

In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.
Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.
Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are 
multiple answers, return the lexicographically smallest one.

Example:
Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

Note:
nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
'''

class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        n, max3, ans = len(nums), 0, []
        presum = [0] * (n+1)
        for i in range(n):
            presum[i+1] = presum[i] + nums[i]
        max_lsum, max_rsum = presum[k], presum[n] - presum[n-k]
        left, right = [0] * n, [0] * n
        right[n-k] = n-k
        for i in range(k, n - 2*k + 1):
            cur_lsum, cur_rsum = presum[i+1] - presum[i+1-k], presum[n-1-i+k] - presum[n-1-i]
            if cur_lsum > max_lsum: left[i], max_lsum = i+1-k, cur_lsum
            else: left[i] = left[i-1]
            if cur_rsum > max_rsum: right[n-1-i], max_rsum = n-1-i, cur_rsum
            else: right[n-1-i] = right[n-i]
        for i in range(k, n - 2*k + 1):
            l, r = left[i-1], right[i+k]
            sum3 = (presum[l+k] - presum[l]) + (presum[i+k] - presum[i]) + (presum[r+k]-presum[r])
            if sum3 > max3:
                max3, ans = sum3, [l, i, r]
        return ans


if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    ans = sol.maxSumOfThreeSubarrays([7,13,20,19,19,2,10,1,1,19], 3)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

