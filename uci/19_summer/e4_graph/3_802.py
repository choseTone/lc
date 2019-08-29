__author__ = 'wangqc'

# https://leetcode.com/problems/find-eventual-safe-states/

from collections import Counter


class Solution:
    def eventualSafeNodes(self, graph):
        memo = Counter()

        def dfs(node):
            if memo[node]:
                return memo[node] == 2
            memo[node] = 1
            for nei in graph[node]:
                if memo[nei] == 1 or (not memo[nei] and not dfs(nei)):
                    return False
            memo[node] = 2
            return True

        return list(filter(dfs, range(len(graph))))


if __name__ == '__main__':
    sol = Solution()

    t1 = [[1, 2], [2, 3], [5], [0], [5], [], []],
    print(sol.eventualSafeNodes(*t1))
