__author__ = 'wangqc'

# https://leetcode.com/problems/redundant-connection-ii/


class Solution:
    def findRedundantDirectedConnection(self, edges):
        N, p1, p2, c = len(edges), None, None, None
        p = [0] * (N+1)
        for i, (s, d) in enumerate(edges):
            if p[d]:
                p1, p2, c, edges[i][0] = p[d], s, d, 0
            else:
                p[d] = s

        p = list(range(N+1))

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        for s, d in edges:
            if s:
                ps, pd = find(s), find(d)
                if ps == pd:
                    return p1 and [p1, c] or [s, d]
                else:
                    p[pd] = ps
        return [p2, c]


if __name__ == '__main__':
    sol = Solution()

    t1 = [[2,1],[3,1],[4,2],[1,4]],
    print(sol.findRedundantDirectedConnection(*t1))

    t2 = [[1,2],[2,3],[3,4],[4,1],[1,5]],
    print(sol.findRedundantDirectedConnection(*t2))