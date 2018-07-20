__author__ = 'wangqc'

'''
240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example:
Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''


class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix: return False
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n-1
        while col >= 0 and row < m:
            if matrix[row][col] < target: row += 1
            elif matrix[row][col] > target: col -= 1
            else: return True
        return False


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()

    matrix = [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    ans = sol.searchMatrix(matrix, 25)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
