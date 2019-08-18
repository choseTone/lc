__author__ = 'wangqc'
# https://leetcode.com/problems/last-stone-weight/

import heapq


class Solution:
    def lastStoneWeight(self, stones):
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a, b = heapq.heappop(stones), heapq.heappop(stones)
            if a < b:
                heapq.heappush(stones, a-b)
        return -stones[0] if stones else 0

if __name__ == '__main__':
    sol = Solution()

    t1 = [2,7,4,1,8,1],
    print(sol.lastStoneWeight(*t1))
