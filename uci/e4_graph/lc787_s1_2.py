__author__ = 'wangqc'

# https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/267200/Python-Dijkstra

import collections, heapq

def findCheapestPrice(n, flights, src, dst, K):
	pq, g = [(0,src,K+1)], collections.defaultdict(dict)
	for s,d,c in flights: g[s][d] = c
	while pq:
		cost, s, k = heapq.heappop(pq)
		if s == dst: return cost
		if k:
			for d in g[s]:
				heapq.heappush(pq, (cost+g[s][d], d, k-1))
	return -1