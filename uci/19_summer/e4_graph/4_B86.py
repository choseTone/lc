__author__ = 'wangqc'

# https://leetcode.com/problems/optimize-water-distribution-in-a-village/

from collections import defaultdict
import heapq


class Solution:
    def minCostToSupplyWaterKruskal(self, n, wells, pipes):
        p = list(range(n+1))

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                p[py] = px
                return True
            return False

        cost, undone = 0, n
        for u, v, w in sorted([[0,i,w] for i, w in enumerate(wells,1)] + pipes, key=lambda x:x[2]):
            if union(u, v):
                cost += w
                undone -= 1
            if not undone:
                break
        return cost

    def minCostToSupplyWaterPrim(self, n, wells, pipes):
        seen, graph = set(), defaultdict(dict)
        for u, v, w in pipes:
            graph[u][v] = graph[v][u] = min(graph[v].get(u, float('inf')), w)
        cost, undone, pq = 0, n, [(w, i) for i, w in enumerate(wells, 1)]
        heapq.heapify(pq)
        while pq:
            c, x = heapq.heappop(pq)
            if x not in seen:
                cost += c
                undone -= 1
                if not undone:
                    break
                seen.add(x)
                for y, w in graph[x].items():
                    if y not in seen:
                        heapq.heappush(pq, (w, y))
        return cost


if __name__ == '__main__':
    sol = Solution()

    t1 = 3, [1,2,2], [[1,2,1],[2,3,1]],
    print(sol.minCostToSupplyWaterKruskal(*t1))
    print(sol.minCostToSupplyWaterPrim(*t1))