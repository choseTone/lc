__author__ = 'wangqc'

'''
85. Maximal Rectangle

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''


class Solution:
    def maximalRectangle(self, matrix):
        ans = 0
        if matrix and matrix[0]:
            width = len(matrix[0])
            hist = [0] * (width + 1)
            for row in matrix:
                for i in range(width):
                    hist[i] = hist[i] + 1 if row[i] == '1' else 0
                stack = [-1]
                for j in range(width+1):
                    while hist[j] < hist[stack[-1]]:
                        height = hist[stack.pop()]
                        ans = max(ans, height * (j-1-stack[-1]))
                    stack.append(j)
        return ans



if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()

    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    ans = sol.maximalRectangle(matrix)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
