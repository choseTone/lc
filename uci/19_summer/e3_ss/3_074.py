__author__ = 'wangqc'

# https://leetcode.com/problems/search-a-2d-matrix/

import bisect


class Solution:
    def searchMatrix(self, matrix, target):
        if not (matrix and matrix[0]):
            return False
        i = bisect.bisect([row[0] for row in matrix], target) - 1
        if i < 0:
            return False
        j = bisect.bisect(matrix[i], target) - 1
        return j >= 0 and matrix[i][j] == target


if __name__ == '__main__':
    sol = Solution()
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    print(sol.searchMatrix(matrix, 0))
    print(sol.searchMatrix(matrix, 13))
    print(sol.searchMatrix(matrix, 34))
    print(sol.searchMatrix(matrix, 51))
