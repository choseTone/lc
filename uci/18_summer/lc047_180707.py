__author__ = 'wangqc'

'''
47. Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''


class Solution:
    # use (p + [n]).index(n) instead of len(p + 1) to wipe out duplicate permutations
    def permuteUnique(self, nums):
        ans = [[]]
        for n in nums:
            ans = [p[:i] + [n] + p[i:] for p in ans for i in range((p + [n]).index(n) + 1)]
        return ans


if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.permuteUnique([1, 1, 2])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))