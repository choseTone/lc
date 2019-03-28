__author__ = 'wangqc'

# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/discuss/262279/Python-Binary-Search-Need-to-Return-the-Smallest-Candidate

def findKthNumber(m, n, k):
	if m > n: m, n = n, m
	lo, hi = 1, m*n
	while lo < hi:
		mid = lo + hi >> 1
		if sum(min(mid//r, n) for r in range(1,m+1)) < k: lo = mid + 1
		else: hi = mid
	return lo