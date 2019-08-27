__author__ = 'wangqc'


# https://leetcode.com/problems/as-far-from-land-as-possible/

class Solution:
    def maxDistance(self, grid):
        N = len(grid)
        q = [(i,j) for i in range(N) for j in range(N) if grid[i][j]]
        if len(q) in (N*N, 0):
            return -1
        for i, j in q:
            for x, y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if 0 <= x < N and 0 <= y < N and not grid[x][y]:
                    grid[x][y] = grid[i][j] + 1
                    q.append((x,y))
        i, j = q[-1]
        return grid[i][j]-1


if __name__ == '__main__':
    sol = Solution()

    t1 = [[1,0,1],[0,0,0],[1,0,1]],
    print(sol.maxDistance(*t1))

    t2 = [[1,0,0],[0,0,0],[0,0,0]],
    print(sol.maxDistance(*t2))

    t3 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
    print(sol.maxDistance(*t3))

    t4 = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]],
    print(sol.maxDistance(*t4))
