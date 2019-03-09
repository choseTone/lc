__author__ = 'wangqc'

'''
407. Trapping Rain Water II

Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the 
volume of water it is able to trap after raining.

Note:
Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.
'''

import heapq

class Solution:
    def trapRainWater(self, heightMap):
        while not heightMap: return 0
        m, n, ans = len(heightMap), len(heightMap[0]), 0
        visited, lowest = [[False] * n for _ in range(m)], []
        for i in range(m):
            heapq.heappush(lowest, (heightMap[i][0], i, 0))
            heapq.heappush(lowest, (heightMap[i][n-1], i, n-1))
            visited[i][0] = visited[i][n-1] = True
        for j in range(n):
            heapq.heappush(lowest, (heightMap[0][j], 0, j))
            heapq.heappush(lowest, (heightMap[m-1][j], m-1, j))
            visited[0][j] = visited[m-1][j] = True
        while lowest:
            curr, i, j = heapq.heappop(lowest)
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    ans += max(0, curr - heightMap[x][y])
                    visited[x][y] = True
                    heapq.heappush(lowest, (max(curr, heightMap[x][y]), x, y))
        return ans



if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    heightMap = [
      [1,4,3,1,3,2],
      [3,2,1,3,2,4],
      [2,3,3,2,3,1]
    ]
    ans = sol.trapRainWater(heightMap)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

