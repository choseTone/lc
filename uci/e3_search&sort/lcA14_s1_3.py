__author__ = 'wangqc'

# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/259177/Python-Binary-Search

def shipWithinDays(weights, D):
	avg = sum(weights) // D
	l, r = max(max(weights), avg), 2*avg
	while l < r:
		cap, load, days = l + r >> 1, 0, 1
		for w in weights:
			if load + w > cap: load, days = 0, days+1
			if days > D: break
			load += w
		if days > D: l = cap + 1
		else: r = cap
	return l