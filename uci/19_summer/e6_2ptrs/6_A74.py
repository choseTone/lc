__author__ = 'wangqc'

# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/


from collections import Counter


class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            for j in range(1, N):
                matrix[i][j] += matrix[i][j-1]
        cnt = 0
        for i in range(M):
            presum = [0] * N
            for j in range(i, M):
                gap = Counter({0:1})
                for k in range(N):
                    presum[k] += matrix[j][k]
                    cnt += gap[presum[k]-target]
                    gap[presum[k]] += 1
        return cnt


if __name__ == '__main__':
    sol = Solution()

    t1 = [[0,1,0],[1,1,1],[0,1,0]], 0,
    print(sol.numSubmatrixSumTarget(*t1))

    t2 = [[1,-1],[-1,1]], 0,
    print(sol.numSubmatrixSumTarget(*t2))

    t3 = [[0,1,1,1,0,1],[0,0,0,0,0,1],[0,0,1,0,0,1],[1,1,0,1,1,0],[1,0,0,1,0,0]], 0,
    print(sol.numSubmatrixSumTarget(*t3))