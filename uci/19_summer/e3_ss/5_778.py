__author__ = 'wangqc'

# https://leetcode.com/problems/swim-in-rising-water/

import heapq


class Solution:
    def swimInWater(self, grid):
        N, pq, min_t = len(grid), [(grid[0][0], 0, 0)], 0
        while pq:
            t, i, j = heapq.heappop(pq)
            min_t = max(t, min_t)
            if i == j == N-1:
                break
            for x, y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if 0 <= x < N and 0 <= y < N and grid[x][y] >= 0:
                    heapq.heappush(pq, (grid[x][y], x, y))
                    grid[x][y] = -1
        return min_t


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

