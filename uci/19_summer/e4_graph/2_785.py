__author__ = 'wangqc'

# https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph):
        seen, N = {}, len(graph)
        def dfs(node, g):
            if node in seen:
                return seen[node] == g
            seen[node] = g
            return all(dfs(nei, 1-g) for nei in graph[node])
        return all(dfs(node, 0) for node in range(N) if node not in seen)


if __name__ == '__main__':
    sol = Solution()

    t1 = [[1,3], [0,2], [1,3], [0,2]],
    print(sol.isBipartite(*t1))

    t2 = [[1,2,3], [0,2], [0,1,3], [0,2]],
    print(sol.isBipartite(*t2))