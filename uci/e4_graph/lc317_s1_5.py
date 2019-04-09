__author__ = 'wangqc'

# https://leetcode.com/problems/shortest-distance-from-all-buildings/discuss/269475/Python-BFS-from-Buildings

def shortestDistance(grid):
	m, n, tot = len(grid), len(grid) and len(grid[0]), sum(1 for row in grid for col in row if col == 1)
	bld, dst = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]
	def bfs(i,j):
		seen, cnt, q = {(i,j)}, 1, [(i,j,1)]
		for i, j, d in q:
			for x, y in ((i-1,j), (i+1,j), (i,j-1), (i, j+1)):
				if 0 <= x < m and 0 <= y < n and grid[x][y] != 2 and (x,y) not in seen:
					seen.add((x,y))
					if not grid[x][y]:
						bld[x][y], dst[x][y] = bld[x][y]+1, dst[x][y]+d
						q.append((x,y,d+1))
					else: cnt += 1
		return cnt == tot
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1 and not bfs(i,j): return -1
	return min((dst[i][j] for i in range(m) for j in range(n) if not grid[i][j] and bld[i][j]==tot), default=-1)