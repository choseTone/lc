__author__ = 'wangqc'

# https://leetcode.com/problems/the-maze-ii/

import heapq


class Solution:
    def shortestDistance(self, maze, start, destination):
        M, N, src, dst = len(maze), len(maze[0]), tuple(start), tuple(destination)
        pq, reached = [(0, src)], {src: 0}
        while pq:
            d, s = heapq.heappop(pq)
            if s == dst:
                return d
            reached[s] = d
            for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                x, y, dd = *s, 0
                while 0 <= x+dx < M and 0 <= y+dy < N and not maze[x+dx][y+dy]:
                    x += dx
                    y += dy
                    dd += 1
                if (x, y) not in reached or reached[x,y] > d+dd:
                    heapq.heappush(pq, (d+dd, (x, y)))
        return -1


if __name__ == '__main__':
    sol = Solution()

    t1 = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [4,4],
    print(sol.shortestDistance(*t1))

    t2 = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [3,2],
    print(sol.shortestDistance(*t2))
