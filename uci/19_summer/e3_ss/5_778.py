__author__ = 'wangqc'

# https://leetcode.com/problems/swim-in-rising-water/

import heapq

class Solution:
    def swimInWater(self, grid):
        # search from (N-1,N-1) to (0,0)
        # as min-heap tends to pop smaller x,y coordinates points
        N, min_t = len(grid), grid[0][0]
        pq = [(grid[N-1][N-1], N-1, N-1)]
        while pq:
            t, i, j = heapq.heappop(pq)
            min_t = max(t, min_t)
            for x, y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if x == y == 0:
                    return min_t
                if 0 <= x < N and 0 <= y < N and grid[x][y] >= 0:
                    heapq.heappush(pq, (grid[x][y], x, y))
                    grid[x][y] = -1


if __name__ == '__main__':
    sol = Solution()

    t1 = [
             [0,  1, 2, 3, 4],
             [24,23,22,21, 5],
             [12,13,14,15,16],
             [11,17,18,19,20],
             [10, 9, 8, 7, 6]
         ],
    print(sol.swimInWater(*t1))

