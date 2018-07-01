__author__ = 'wangqc'

'''
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and 
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount 
of money you can rob tonight without alerting the police.

Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
             
Example 2:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
'''


class Solution:
    def rob(self, nums):
        n = len(nums)
        if n < 2: return n and nums[0]
        # use dp to update two variables cur_max and prev_max
        cur_max, prev_max = nums[0], 0
        for i in range(1, n):
            tmp, prev_max = prev_max, cur_max
            cur_max = max(tmp + nums[i], cur_max)
        return cur_max


if __name__ == '__main__':
    from time import time
    from random import randint

    sol = Solution()
    nums = [randint(1, 20) for _ in range(20)]
    t = time()
    ans = sol.rob(nums)
    # input: [7, 11, 14, 8, 15, 6, 1, 11, 8, 16, 11, 5, 5, 17, 20, 9, 13, 9, 16, 10]; ans: 117
    print('input: %s\nans: %s\ntime: %.3fms' % (nums, ans, ((time() - t)) * 1000))