__author__ = 'wangqc'

# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/


class Solution:
    def maximumSum(self, arr):
        s1 = s2 = min1 = min2 = 0
        max_min_sum = float('-inf')
        for x in arr:
            if s1 <= 0:
                s1 = min1 = 0
            if s2 <= min2:
                s2 = min2 = 0
            s1, s2 = s1 + x, s2 + x
            max_min_sum = max(max_min_sum, s1 - min1, s2 - min2)
            min1, min2 = min(min1, x), min(min2, x)
        return max_min_sum


if __name__ == '__main__':
    sol = Solution()

    t1 = [1,-2,0,3],
    print(sol.maximumSum(*t1))

    t2 = [-1,-1,-1,-1],
    print(sol.maximumSum(*t2))

    t3 = [-8,7,-12,-1,0,11,-2,-3,4,-13,2,3,-6],
    print(sol.maximumSum(*t3))