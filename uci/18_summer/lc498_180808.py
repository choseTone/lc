__author__ = 'wangqc'

'''
498. Diagonal Traverse

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]

Note:
The total number of elements of the given matrix will not exceed 10,000.
'''

class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        if m == 1: return matrix[0]
        if n == 1: return [matrix[i][0] for i in range(m)]
        i, j, reverse, ans = 0, 0, False, []
        for _ in range(m * n):
            ans.append(matrix[i][j])
            if reverse and i < m - 1 and j == 0 or not reverse and j == n - 1:
                i += 1
                reverse = not reverse
            elif reverse and i == m - 1 or not reverse and i == 0:
                j += 1
                reverse = not reverse
            else:
                i, j = (i+1, j-1) if reverse else (i-1, j+1)
        return ans


if __name__ == '__main__':
    from time import time

    sol = Solution()
    matrix = [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    t = time()
    ans = sol.findDiagonalOrder([[1,2],[3,4]])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
