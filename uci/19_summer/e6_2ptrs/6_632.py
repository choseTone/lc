__author__ = 'wangqc'

# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/


import heapq


class Solution:
    def smallestRange(self, nums):
        candidates = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(candidates)
        s_range = -1e6, 1e6,
        hi = max(row[0] for row in nums)
        while candidates:
            lo, i, j = heapq.heappop(candidates)
            s_range = min((s_range, (lo, hi)), key=lambda x: x[1]-x[0])
            if j == len(nums[i]) - 1:
                return s_range
            val = nums[i][j+1]
            hi = max(hi, val)
            heapq.heappush(candidates, (val, i, j+1))


if __name__ == '__main__':
    sol = Solution()

    t1 = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]],
    print(sol.smallestRange(*t1))