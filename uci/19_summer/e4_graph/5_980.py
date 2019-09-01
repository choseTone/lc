__author__ = 'wangqc'

# https://leetcode.com/problems/unique-paths-iii/


class Solution:
    def uniquePathsIII(self, grid):
        M, N, self.cnt = len(grid), len(grid[0]), 0
        def dfs(i,j,k):
            grid[i][j] = -1
            for x, y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if 0 <= x < M and 0 <= y < N:
                    if not grid[x][y]:
                        dfs(x, y, k-1)
                    if grid[x][y] == 2 and not k:
                        self.cnt += 1
            grid[i][j] = 0

        flat = sum(grid, [])
        dfs(*divmod(flat.index(1), N), flat.count(0))
        return self.cnt




if __name__ == '__main__':
    sol = Solution()

    t1 = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]],
    print(sol.uniquePathsIII(*t1))

    t2 = [[1,0,0,0],[0,0,0,0],[0,0,0,2]],
    print(sol.uniquePathsIII(*t2))

    t3 = [[0,1],[2,0]],
    print(sol.uniquePathsIII(*t3))