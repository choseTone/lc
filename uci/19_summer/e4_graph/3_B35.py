__author__ = 'wangqc'

# https://leetcode.com/problems/connecting-cities-with-minimum-cost/

from collections import defaultdict


class Solution:
    def minimumCost(self, N, conections):
        p, g, cost = list(range(N+1)), N-1, 0

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                p[py] = px
                return True
            return False

        for x, y, c in sorted(conections, key=lambda x:x[2]):
            if union(x, y):
                cost += c
                g -= 1
            if not g:
                return cost
        return -1


if __name__ == '__main__':
    sol = Solution()

    t1 = 3, [[1,2,5],[1,3,6],[2,3,1]],
    print(sol.minimumCost(*t1))
