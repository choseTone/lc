__author__ = 'wangqc'


# https://leetcode.com/problems/number-of-islands/


class Solution:
    def numIslands(self, grid):
        M, N = len(grid), len(grid) and len(grid[0])

        def dfs(i, j):
            for x, y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if 0 <= x < M and 0 <= y < N and grid[x][y] == "1":
                    grid[x][y] = "0"
                    dfs(x, y)
            return 1

        def bfs(i, j):
            q, grid[i][j] = [(i, j)], "0"
            for i, j in q:
                for x, y in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
                    if 0 <= x < M and 0 <= y < N and grid[x][y] == "1":
                        grid[x][y] = "0"
                        q.append((x, y))
            return 1

        # return sum(dfs(i,j) for i in range(M) for j in range(N) if grid[i][j] == "1")
        return sum(bfs(i,j) for i in range(M) for j in range(N) if grid[i][j] == "1")


if __name__ == '__main__':
    sol = Solution()

    t1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]],
    print(sol.numIslands(*t1))

    t2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]],
    print(sol.numIslands(*t2))
