__author__ = 'wangqc'

# https://leetcode.com/problems/maximal-rectangle/


class Solution:
    def maximalRectangle(self, matrix):
        sz, N = 0, len(matrix) and len(matrix[0])
        heights = [0] * (N+1)
        for row in matrix:
            for i in range(N):
                heights[i] = heights[i] + 1 if row[i] == "1" else 0
            widths = [-1]
            for j in range(N+1):
                while heights[j] < heights[widths[-1]]:
                    height = heights[widths.pop()]
                    if height > heights[widths[-1]]:
                        sz = max(sz, height*(j-1-widths[-1]))
                widths.append(j)
        return sz


if __name__ == '__main__':
    sol = Solution()
    t1 = [
             ["1", "0", "1", "0", "0"],
             ["1", "0", "1", "1", "1"],
             ["1", "1", "1", "1", "1"],
             ["1", "0", "0", "1", "0"]
         ],
    print(sol.maximalRectangle(*t1))