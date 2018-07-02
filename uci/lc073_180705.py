__author__ = 'wangqc'

'''
73. Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:
Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''


class Solution:
    # scan matrix in order and set m[i][0] and m[0][j] to 0 if m[i][j] is 0 as the row and col markers
    # then scan matrix to set m[i][j] to 0 if any one of the two markers is 0 (means there is a 0 from same row or col)
    # second scan need to be done reversely otherwise m[i][0] would be scanned first and corrupted by m[i-k][0]
    # and then wrongly set whole m[i] to 0
    # need to independently handle the first row since m[0][0] would be corrupted by first col's zero elements
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        row1_has_0 = not all(matrix[0])
        for i in range(1, m):
            for j in range(n):
                if not matrix[i][j]:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, m)[::-1]:
            for j in range(n)[::-1]:
                if not (matrix[i][0] and matrix[0][j]):
                    matrix[i][j] = 0
        if row1_has_0:
            matrix[0] = [0] * n


if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    sol.setZeroes(matrix)
    print('ans: %s\ntime: %.3fms' % (matrix, ((time() - t)) * 1000))
