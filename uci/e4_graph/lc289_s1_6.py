__author__ = 'wangqc'

# https://leetcode.com/problems/best-meeting-point/discuss/271017/Python-Distance-to-Median

def minTotalDistance(grid):
	m, n = len(grid), len(grid) and len(grid[0])
	rows, cols = [i for i in range(m) for j in range(n) if grid[i][j]], [j for j in range(n) for i in range(m) if grid[i][j]]
	def dist(A):
		i, j, d = 0, len(A)-1, 0
		while i < j:
			d, i, j = d+A[j]-A[i], i+1, j-1
		return d
	return dist(rows) + dist(cols)
