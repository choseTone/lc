__author__ = 'wangqc'


# https://leetcode.com/problems/minesweeper/

class Solution:
    def numDistinctIslands(self, grid):
        M, N = len(grid), len(grid[0])
        def dfs(i, j, shape):
            if 0 <= i < M and 0 <= j < N and grid[i][j]:
                grid[i][j] = 0
                return shape + dfs(i-1,j,"u") + "d" + dfs(i+1,j,"d") + "u" + dfs(i,j-1,"l") + "r" + dfs(i,j+1,"r") + "l"
            return ""
        return len({dfs(i,j,"") for i in range(M) for j in range(N) if grid[i][j]})



if __name__ == '__main__':
    sol = Solution()

    t1 = [
             [1, 1, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 0, 0, 1, 1],
             [0, 0, 0, 1, 1]
         ],
    print(sol.numDistinctIslands(*t1))

    t2 = [
             [1, 1, 0, 1, 1],
             [1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1],
             [1, 1, 0, 1, 1]
         ],
    print(sol.numDistinctIslands(*t2))

