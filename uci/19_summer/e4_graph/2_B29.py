__author__ = 'wangqc'

# https://leetcode.com/problems/shortest-path-with-alternating-colors/

from collections import defaultdict

class Solution:
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        graph = [defaultdict(set), defaultdict(set)]
        for s, d in red_edges:
            graph[0][s].add(d)
        for s, d in blue_edges:
            graph[1][s].add(d)
        paths, q, seen = [0] + [-1]*(n-1), [(0,0,0), (0,0,1)], set()
        for node, d, color in q:
            for nei in graph[color][node]:
                if (nei, 1-color) not in seen:
                    if paths[nei] < 0:
                        paths[nei] = d + 1
                    q.append((nei, d+1, 1-color))
                    seen.add((nei, 1-color))
        return paths






if __name__ == '__main__':
    sol = Solution()

    t1 = 3, [[0,1]], [[2,1]],
    print(sol.shortestAlternatingPaths(*t1))

    t2 = 5, [[0,1],[1,2],[2,3],[3,4]], [[1,2],[2,3],[3,1]],
    print(sol.shortestAlternatingPaths(*t2))