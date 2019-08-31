__author__ = 'wangqc'

# https://leetcode.com/problems/possible-bipartition/

from collections import defaultdict


class Solution:
    def possibleBipartition(self, N, dislikes):
        graph = defaultdict(set)
        for u, v in dislikes:
            graph[u].add(v)
            graph[v].add(u)
        memo = {}

        def dfs(node, g):
            if node in memo:
                return memo[node] == g
            memo[node] = g
            return all(dfs(nei, 1 - g) for nei in graph[node])

        return all(dfs(i, 0) for i in range(1, N + 1) if i not in memo)


if __name__ == '__main__':
    sol = Solution()

    t1 = 4, [[1,2],[1,3],[2,4]],
    print(sol.possibleBipartition(*t1))

    t2 = 5, [[1,2],[2,3],[3,4],[4,5],[1,5]],
    print(sol.possibleBipartition(*t2))
