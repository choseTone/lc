__author__ = 'wangqc'

# https://leetcode.com/problems/walls-and-gates/

from collections import defaultdict


class Solution:
    def wallsAndGates(self, rooms):
        M, N = len(rooms), len(rooms) and len(rooms[0])
        q = [(i,j) for i in range(M) for j in range(N) if not rooms[i][j]]
        for i, j in q:
            for x, y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if 0 <= x < M and 0 <= y < N and rooms[x][y] == 2**31-1:
                    rooms[x][y] = rooms[i][j] + 1
                    q.append((x,y))

if __name__ == '__main__':
    sol = Solution()

    room = [
             [2147483647,-1,0,2147483647],
             [2147483647,2147483647,2147483647,-1],
             [2147483647,-1,2147483647,-1],
             [0,-1,2147483647,2147483647]
         ]
    sol.wallsAndGates(room)
    for row in room:
        print(row)
