__author__ = 'wangqc'

# https://leetcode.com/problems/largest-plus-sign/discuss/260364/Python-Linear-%2B-Binary-Search

import bisect

def orderOfLargestPlusSign(N, mines):
	rows, cols, sz = [[-1,N] for _ in range(N)], [[-1,N] for _ in range(N)], 0
	for r, c in mines:
		bisect.insort(rows[r], c)
		bisect.insort(cols[c], r)
	for y, row in enumerate(rows):
		for i in range(len(row)-1):
			l, r = row[i], row[i+1]
			for x in range(l+sz+1, r-sz):
				j = bisect.bisect(cols[x], y)
				t, b = cols[x][j-1], cols[x][j]
				sz = max(sz, min(x-l, r-x, y-t, b-y))
	return sz