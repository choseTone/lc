__author__ = 'wangqc'

# https://leetcode.com/problems/koko-eating-bananas/discuss/262311/Python-Binary-Search-Narrow-Down-Search-Space

import math

def minEatingSpeed(piles, H):
	s = sum(piles)
	lo = math.ceil(s/H)
	hi = min(max(piles), math.ceil(s/(H-len(piles)+1)))
	while lo < hi:
		mid = lo + hi >> 1
		if sum(math.ceil(p/mid) for p in piles) > H: lo = mid + 1
		else: hi = mid
	return lo