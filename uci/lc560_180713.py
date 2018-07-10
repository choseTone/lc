__author__ = 'wangqc'

'''
560. Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous subarrays
whose sum equals to k.

Example 1:
Input:nums = [1, 1, 1], k = 2
Output: 2

Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''


class Solution:
    # counter counts the number of subarrays begin with nums[0] whose sums equals to the key
    # if i > j and sum(ai:aj) = k, then sum(a0:ai) - sum(a0:aj) = k
    def subarraySum(self, nums, k):
        counter, cur_sum, ans = {0: 1}, 0, 0
        for n in nums:
            cur_sum += n
            ans += counter.get(cur_sum - k, 0)
            counter[cur_sum] = counter.get(cur_sum, 0) + 1
        return ans


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.subarraySum([1, 1, 1], 2)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))