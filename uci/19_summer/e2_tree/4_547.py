__author__ = 'wangqc'


# https://leetcode.com/problems/friend-circles/

from collections import defaultdict

class Solution:
    def findCircleNum(self, M):
        graph, seen, n = defaultdict(set), set(), len(M)
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j]:
                    graph[i].add(j)
                    graph[j].add(i)

        def dfs(node):
            if node not in seen:
                seen.add(node)
                for nei in graph[node]:
                    dfs(nei)
            return 1

        def bfs(queue):
            seen.add(queue[0])
            for node in queue:
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)
            return 1

        # return sum(dfs(node) for node in range(n) if node not in seen)
        return sum(bfs([node]) for node in range(n) if node not in seen)

    def findCircleNumUF(self, M):
        n = len(M)
        p, rank = list(range(n)), [0]*n

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if rank[px] < rank[py]:
                    px, py = py, px
                p[py] = px
                rank[px] += 1

        for i in range(n):
            for j in range(i+1, n):
                if M[i][j]: union(i, j)
        return len(set(map(find, range(n))))


if __name__ == '__main__':
    sol = Solution()

    t1 = [[1,1,0],[1,1,0],[0,0,1]],
    print(sol.findCircleNum(*t1))
    print(sol.findCircleNumUF(*t1))

    t2 = [[1,1,0],[1,1,1],[0,1,1]],
    print(sol.findCircleNum(*t2))
    print(sol.findCircleNumUF(*t2))