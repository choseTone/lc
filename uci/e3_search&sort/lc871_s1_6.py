__author__ = 'wangqc'

# https://leetcode.com/problems/minimum-number-of-refueling-stops/discuss/263468/Python-Max-Heap-O(NlogN)

import heapq

def minRefuelStops(target, stock, stations):
	h, sour, cnt = [], 0, 0
	for dest, gas in stations + [[target, float('inf')]]:
		stock -= dest-sour
		while h and stock < 0:
			stock -= heapq.heappop(h)
			cnt += 1
		if stock < 0: return -1
		heapq.heappush(h, -gas)
		sour = dest
	return cnt