__author__ = 'wangqc'

'''
778. Swim in Rising Water

On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).
Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 
4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim 
infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.
You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:
Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.

Example 2:
Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

Note:
2 <= N <= 50.
grid[i][j] is a permutation of [0, ..., N*N - 1].
'''

import heapq

class Solution:
    def swimInWater(self, grid):
        n, seen, pq, ans = len(grid), {(0, 0)}, [(grid[0][0], 0, 0)], 0
        # choose the smallest node within the extent
        while pq:
            d, i, j = heapq.heappop(pq)
            ans = max(d, ans)
            if i == j == n-1: return ans
            for x, y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if 0 <= x < n and 0 <= y < n and (x,y) not in seen: # expand
                    seen.add((x, y))
                    heapq.heappush(pq, (grid[x][y], x, y))


if __name__ == '__main__':
    sol = Solution()
    argv = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    ans = sol.swimInWater(argv)
    print('Input : %s\nOutput: %s' % (argv, ans))

