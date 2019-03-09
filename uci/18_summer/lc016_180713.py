__author__ = 'wangqc'

'''
16. 3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to
target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n, cand = len(nums), set()
        for i in range(n-2):
            head = nums[i]
            hit, num1, l, r = target - head, nums[i], i+1, n-1
            smallest, largest = nums[l] + nums[l+1], nums[r-1] + nums[r]
            if smallest > hit: cand.add(head + smallest)
            elif largest < hit: cand.add(head + largest)
            else:
                min_gap = nums[l] + nums[r] - hit
                while l < r:
                    gap = nums[l] + nums[r] - hit
                    min_gap = min(min_gap, gap, key=lambda x: abs(x))
                    if gap == 0: return target
                    elif gap < 0: l += 1
                    else: r -= 1
                cand.add(min_gap + target)
        return sorted(cand, key=lambda x: abs(x-target))[0]


if __name__ == '__main__':
    from time import time
    from random import randint
    sol = Solution()
    t = time()
    nums = [randint(-100, 100) for _ in range(20)]
    ans = sol.threeSumClosest(nums, 6)
    print('nums: %s\nans: %s\ntime: %.3fms' % (nums, ans, ((time() - t)) * 1000))