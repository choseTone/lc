__author__ = 'wangqc'


# https://leetcode.com/problems/path-with-maximum-minimum-value/

import heapq

class Solution:
    def maximumMinimumPath(self, A):
        M, N, score = len(A), len(A[0]), A[0][0]
        cand, A[M-1][N-1] = [(-A[M-1][N-1], M-1, N-1)], -1
        while cand:
            v, i, j = heapq.heappop(cand)
            score = min(score, -v)
            for x, y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if x == y == 0:
                    return score
                if 0 <= x < M and 0 <= y < N and A[x][y] >= 0:
                    heapq.heappush(cand, (-A[x][y], x, y))
                    A[x][y] = -1





if __name__ == '__main__':
    sol = Solution()

    t1 = [[5,4,5],[1,2,6],[7,4,6]],
    print(sol.maximumMinimumPath(*t1))

    t2 = [[2,2,1,2,2,2],[1,2,2,2,1,2]],
    print(sol.maximumMinimumPath(*t2))

    t3 = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]],
    print(sol.maximumMinimumPath(*t3))
