__author__ = 'wangqc'

# https://leetcode.com/problems/continuous-subarray-sum/


class Solution:
    def checkSubarraySum(self, nums, k):
        agg, prev = 0, {0: -1}
        for i in range(len(nums)):
            agg = (agg + nums[i]) % (k or float('inf'))
            if i - prev.setdefault(agg, i) > 1:
                return True
        return False


if __name__ == '__main__':
    sol = Solution()

    t1 = [23, 2, 4, 6, 7], 6,
    print(sol.checkSubarraySum(*t1))

    t2 = [23, 2, 6, 4, 7], 6,
    print(sol.checkSubarraySum(*t2))
