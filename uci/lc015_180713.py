__author__ = 'wangqc'

'''
15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets
in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution:
    # convert nums list to a freq counter and separate the counter in neg set and non-neg set
    def threeSum(self, nums):
        if len(nums) < 3: return []
        cache = {}
        for n in nums:
            cache[n] = cache.get(n, 0) + 1
        ans = [[0, 0, 0]] if cache.get(0, 0) > 2 else []
        negs, non_negs = list(filter(lambda x: x<0, cache)), list(filter(lambda x: x>=0, cache))
        for n in negs:
            for nn in non_negs:
                target = -(n + nn)
                if target in cache:
                    if target in {n, nn} and cache[target] > 1:
                        ans.append([n, target, nn])
                    elif target < n:
                        ans.append([target, n, nn])
                    elif target > nn:
                        ans.append([target, n, nn])
        return ans


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.threeSum([-1,-1,2])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))