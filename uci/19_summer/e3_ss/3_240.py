__author__ = 'wangqc'


# https://leetcode.com/problems/search-a-2d-matrix-ii/


class Solution:
    def searchMatrix(self, matrix, target):
        M, N = len(matrix), len(matrix) and len(matrix[0])
        i, j = 0, N - 1
        while i < M and j >= 0:
            if target > matrix[i][j]:
                i += 1
            elif target < matrix[i][j]:
                j -= 1
            else:
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    print(sol.searchMatrix(matrix, 5))
    print(sol.searchMatrix(matrix, 20))
    print(sol.searchMatrix(matrix, 34))
