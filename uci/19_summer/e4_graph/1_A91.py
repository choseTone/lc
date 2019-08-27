__author__ = 'wangqc'


# https://leetcode.com/problems/shortest-path-in-binary-matrix/

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] or grid[-1][-1]:
            return -1
        q, M, N = [(0, 0, 1)], len(grid), len(grid[0])
        for i, j, d in q:
            if i == M - 1 and j == N - 1:
                return d
            for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
                if 0 <= x < M and 0 <= y < N and not grid[x][y]:
                    grid[x][y] = 1
                    q.append((x, y, d+1))
        return -1


if __name__ == '__main__':
    sol = Solution()

    t1 = [[0]],
    print(sol.shortestPathBinaryMatrix(*t1))

    t2 = [[0,0,0],[1,1,0],[1,1,0]],
    print(sol.shortestPathBinaryMatrix(*t2))

    t3 = [[0,0,0,0,1],[1,0,0,0,0],[0,1,0,1,0],[0,0,0,1,1],[0,0,0,1,0]],
    print(sol.shortestPathBinaryMatrix(*t3))
