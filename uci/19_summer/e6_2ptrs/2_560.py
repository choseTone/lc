__author__ = 'wangqc'

# https://leetcode.com/problems/subarray-sum-equals-k/


class Solution:
    def subarraySum(self, nums, k):
        counter, agg, cnt = {0: 1}, 0, 0
        for x in nums:
            agg += x
            cnt += counter.get(agg-k, 0)
            counter[agg] = counter.get(agg, 0) + 1
        return cnt


if __name__ == '__main__':
    sol = Solution()

    t1 = [1,1,1], 2,
    print(sol.subarraySum(*t1))

    t2 = [6,5,0,0], 5,
    print(sol.subarraySum(*t2))