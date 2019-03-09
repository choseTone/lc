__author__ = 'wangqc'

'''
463. Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid 
cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is
exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't
connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and
height don't exceed 100. Determine the perimeter of the island.

Example:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
Answer: 16
'''


class Solution:
    # add 4 for each land cell, if cell's upper neighbor is land, minus 2(bottom of upper cell and top of current cell),
    # if cell's left neighbor is land, minus 2(right of left cell and left of current cell)
    def islandPerimeter(self, grid):
        if not grid: return 0
        ans, m, n = 0, len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans += 4
                    if i > 0 and grid[i-1][j]: ans -= 2
                    if j > 0 and grid[i][j-1]: ans -= 2
        return ans


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
