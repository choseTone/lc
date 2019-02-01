__author__ = 'wangqc'

'''
713. Subarray Product Less Than K

Your are given an array of positive integers nums.
Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
'''


class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        product = 1
        ans = left = 0
        for right, val in enumerate(nums):
            product *= val
            while product >= k:
                product /= nums[left]
                left += 1
            ans += right - left + 1 # add window size directly to avoid o(n) iteration, reduce o(n^2) to o(n)
        return ans

if __name__ == '__main__':
    sol = Solution()
    argv = [10, 5, 2, 6], 100
    ans = sol.numSubarrayProductLessThanK(*argv)
    print('Input : %s\nOutput: %s' % (argv, ans))

