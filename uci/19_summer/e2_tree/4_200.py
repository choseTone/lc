__author__ = 'wangqc'


# https://leetcode.com/problems/number-of-islands/


class Solution:
    def numIslands(self, grid):
        m, n = len(grid), len(grid) and len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
                grid[i][j] = "0"
                for x, y in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
                    dfs(x, y)
                return 1
            return 0

        def bfs(i, j):
            q, grid[i][j] = [(i, j)], "0"
            for i, j in q:
                for x, y in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                        grid[x][y] = "0"
                        q.append((x, y))
            return 1

        # return sum(dfs(i,j) for i in range(m) for j in range(n))
        return sum(bfs(i,j) for i in range(m) for j in range(n) if grid[i][j] == "1")


if __name__ == '__main__':
    sol = Solution()

    t1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]],
    print(sol.numIslands(*t1))

    t2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]],
    print(sol.numIslands(*t2))
