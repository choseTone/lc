__author__ = 'wangqc'

# https://leetcode.com/problems/swim-in-rising-water/discuss/263371/Python-Min-Heap

import heapq

def swimInWater(grid):
	pq, t, n, seen = [(grid[0][0], 0, 0)], 0, len(grid), set()
	while pq:
		d, i, j = heapq.heappop(pq)
		t = max(t, d)
		if i == j == n-1: return t
		seen.add((i, j))
		for x, y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
			if 0 <= x < n and 0 <= y < n and (x,y) not in seen:
				heapq.heappush(pq, (grid[x][y], x, y))