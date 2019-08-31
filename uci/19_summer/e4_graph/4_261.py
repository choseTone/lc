__author__ = 'wangqc'

# https://leetcode.com/problems/minimum-height-trees/


class Solution:
    # N nodes: N-1 edges without cycle

    def findMinHeightTreesBFS(self, n, edges):
        if len(edges) != n - 1:
            return False
        graph = {i:[] for i in range(n)}
        for u, v in edges:
            graph[u].append(v), graph[v].append(u)
        q = [0]
        for node in q:
            q += graph.pop(node, [])
        return not graph

    def findMinHeightTreesUF(self, n, edges):
        if len(edges) != n - 1:
            return False

        p = list(range(n))

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        for u, v in edges:
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            p[pu] = pv
        return True



if __name__ == '__main__':
    sol = Solution()

    t1 = 5, [[0,1], [0,2], [0,3], [1,4]],
    print(sol.findMinHeightTreesBFS(*t1))
    print(sol.findMinHeightTreesUF(*t1))

    t2 = 5, [[0,1], [1,2], [2,3], [1,3], [1,4]],
    print(sol.findMinHeightTreesBFS(*t2))
    print(sol.findMinHeightTreesUF(*t2))
