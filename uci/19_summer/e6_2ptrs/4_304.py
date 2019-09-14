__author__ = 'wangqc'

# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/


class NumMatrix:

    def __init__(self, matrix):
        M, N = len(matrix), len(matrix) and len(matrix[0])
        self.agg = [[0] * (N+1) for _ in range(M+1)]
        for i in range(M):
            for j in range(N):
                self.agg[i+1][j+1] = self.agg[i][j+1] + self.agg[i+1][j] - self.agg[i][j] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        return self.agg[row2+1][col2+1] - self.agg[row1][col2+1] - self.agg[row2+1][col1] + self.agg[row1][col1]


if __name__ == '__main__':
    obj = NumMatrix(
        [
          [3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]
        ]
    )
    print(obj.sumRegion(2, 1, 4, 3))
    print(obj.sumRegion(1, 1, 2, 2))
    print(obj.sumRegion(1, 2, 2, 4))