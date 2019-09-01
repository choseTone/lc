__author__ = 'wangqc'

# https://leetcode.com/problems/bus-routes/

from collections import defaultdict


class Solution:
    def numBusesToDestination(self, routes, S, T):
        if S == T:
            return 0
        graph, routes, N = defaultdict(set), [set(r) for r in routes], len(routes)
        for i in range(N):
            for j in range(i+1, N):
                if routes[i] & routes[j]:
                    graph[i].add(j), graph[j].add(i)
        src = {i for i in range(N) if S in routes[i]}
        dst = {i for i in range(N) if T in routes[i]}
        if src & dst:
            return 1
        q = [(i, 1) for i in src]
        for x, d in q:
            for y in graph[x]:
                if y in dst:
                    return d+1
                if y not in src:
                    src.add(y)
                    q.append((y, d+1))
        return -1


if __name__ == '__main__':
    sol = Solution()

    t1 = [[1, 2, 7], [3, 6, 7]], 1, 6,
    print(sol.numBusesToDestination(*t1))

    t2 = [[1,7],[3,5]], 5, 5,
    print(sol.numBusesToDestination(*t2))
