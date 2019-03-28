__author__ = 'wangqc'

# https://leetcode.com/problems/search-a-2d-matrix/discuss/258221/Python-Row-and-Col-Binary-Search

import bisect

def searchMatrix(matrix, target):
	if not (matrix and matrix[0]): return False
	r = bisect.bisect([r[0] for r in matrix], target) - 1
	if r < 0: return False
	c = bisect.bisect(matrix[r], target) - 1
	return c >= 0 and matrix[r][c] == target