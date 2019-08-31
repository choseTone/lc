__author__ = 'wangqc'

# https://leetcode.com/problems/cheapest-flights-within-k-stops/

from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = defaultdict(dict)
        for s, d, c in flights:
            graph[s][d] = c
        pq, reached = [(0, src, 0)], set()
        while pq:
            cost, s, k = heapq.heappop(pq)
            reached.add(s)
            if s == dst:
                return cost
            if k <= K:
                for d in graph[s]:
                    if d not in reached:
                        heapq.heappush(pq, (cost+graph[s][d], d, k+1))
        return -1



if __name__ == '__main__':
    sol = Solution()

    t1 = 3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1,
    print(sol.findCheapestPrice(*t1))

    t2 = 3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0,
    print(sol.findCheapestPrice(*t2))
