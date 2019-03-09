__author__ = 'wangqc'

'''
200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and 
is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all 
surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
'''


class Solution:
    def numIslands(self, grid):
        m, n = len(grid), len(grid) and len(grid[0])

        def sink(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                grid[i][j] = '0'
                sink(i, j - 1), sink(i, j + 1), sink(i - 1, j), sink(i + 1, j)
                return 1
            return 0

        return sum(sink(i, j) for i in range(m) for j in range(n))


if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.numIslands([['1','1','0','0','0'], ['1','1','0','0','0'], ['0','0','1','0','0'], ['0','0','0','1','1']])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))