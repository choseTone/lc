__author__ = 'wangqc'

'''
18. 4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that 
a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''


class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        self.ans = []
        self.dfs(nums, 4, target, [])
        return self.ans

    def dfs(self, nums, n, target, cand):
        if n > 2:
            for i in range(len(nums)):
                if nums[i] * n > target or nums[-1] * n < target: break
                if i and nums[i] == nums[i-1]: continue
                self.dfs(nums[i+1:], n-1, target-nums[i], cand+[nums[i]])
        else:
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target: l += 1
                elif nums[l] + nums[r] > target: r -= 1
                else:
                    self.ans.append(cand + [nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    l, r = l + 1, r - 1
            return

if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.fourSum([1, 0, -1, 0, -2, 2], 0)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))