__author__ = 'wangqc'
# https://leetcode.com/problems/sum-of-distances-in-tree/

from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, N, edges):
        tree = defaultdict(set)
        for u, v in edges:
            tree[u].add(v)
            tree[v].add(u)
        count, dist = [1] * N, [0] * N

        def dfs_succ(node, parent):
            for child in tree[node]:
                if child != parent:
                    dfs_succ(child, node)
                    count[node] += count[child]
                    dist[node] += dist[child] + count[child]

        def dfs_pred(node, parent):
            for child in tree[node]:
                if child != parent:
                    # Y nodes -- Node -- Child -- X nodes
                    # dist[N] settled, generate dist[C] from dist[N]:
                    # +1 d for all nodes from Y--N, -1 d for all nodes from C--X
                    # so, dist[child] = dist[node] + (N-count[child]) - count[child]
                    dist[child] = dist[node] + N - 2 * count[child]
                    dfs_pred(child, node)

        dfs_succ(0, None)
        dfs_pred(0, None)
        return dist


if __name__ == '__main__':
    sol = Solution()

    t1 = 6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]],
    print(sol.sumOfDistancesInTree(*t1))
