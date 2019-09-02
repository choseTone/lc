__author__ = 'wangqc'

# https://leetcode.com/problems/best-meeting-point/


class Solution:
    def minTotalDistance(self, grid):
        M, N = len(grid), len(grid) and len(grid[0])
        rows = [i for i in range(M) for j in range(N) if grid[i][j]]
        cols = [j for j in range(N) for i in range(M) if grid[i][j]]

        # https://leetcode.com/problems/best-meeting-point/discuss/271017
        def d_from_median(A):
            i, j, d = 0, len(A)-1, 0
            while i < j:
                d += A[j] - A[i]
                i += 1
                j -= 1
            return d

        return d_from_median(rows) + d_from_median(cols)


if __name__ == '__main__':
    sol = Solution()

    t1 = [
             [1,0,0,0,1],
             [0,0,0,0,0],
             [0,0,1,0,0]
         ],
    print(sol.minTotalDistance(*t1))