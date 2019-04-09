__author__ = 'wangqc'

# https://leetcode.com/problems/number-of-islands/discuss/264826/python-dfs

def numIslands(grid):
	m, n = len(grid), len(grid) and len(grid[0])
	def dfs(i,j):
		if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
			grid[i][j] = '0'
			dfs(i-1, j), dfs(i+1, j), dfs(i, j-1), dfs(i, j+1)
			return 1
		return 0
	return sum(dfs(i,j) for i in range(m) for j in range(n))