__author__ = 'wangqc'


# https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid):
        M, N = len(grid), len(grid[0])
        q = [(i,j,0) for i in range(M) for j in range(N) if grid[i][j]==2]
        for i, j, t in q:
            for x, y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if 0 <= x < M and 0 <= y < N and grid[x][y] == 1:
                    grid[x][y] = 2
                    q.append((x,y,t+1))
        return -1 if sum(grid[i][j]==1 for i in range(M) for j in range(N)) else q[-1][2]


if __name__ == '__main__':
    sol = Solution()

    t1 = [[2,1,1],[1,1,0],[0,1,1]],
    print(sol.orangesRotting(*t1))

    t2 = [[2,1,1],[0,1,1],[1,0,1]],
    print(sol.orangesRotting(*t2))

    t3 = [[0,2]],
    print(sol.orangesRotting(*t3))
