__author__ = 'wangqc'

# https://leetcode.com/problems/largest-1-bordered-square/submissions/


class Solution:
    def largest1BorderedSquare(self, grid):
        M, N = len(grid), len(grid[0])
        tops, lefts = [row[:] for row in grid], [row[:] for row in grid]
        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    if i: tops[i][j] = tops[i-1][j] + 1
                    if j: lefts[i][j] = lefts[i][j-1] + 1
        for r in range(min(M,N), 0, -1):
            for i in range(r-1, M):
                for j in range(r-1, N):
                    if min(tops[i][j-r+1], tops[i][j], lefts[i][j], lefts[i-r+1][j]) >= r:
                        return r*r
        return 0


if __name__ == '__main__':
    sol = Solution()

    t1 = [[1,1,1],[1,0,1],[1,1,1]],
    print(sol.largest1BorderedSquare(*t1))

    t2 = [[1,1,0,0]],
    print(sol.largest1BorderedSquare(*t2))