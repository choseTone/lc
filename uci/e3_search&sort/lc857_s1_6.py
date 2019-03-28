__author__ = 'wangqc'

# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/discuss/263402/Python-Sorted-WageQuality-and-Heap

import heapq

def mincostToHireWorkers(quality, wage, K):
	workers = sorted((w/q, w, q) for w, q in zip(wage, quality))
	cost, team, sumq = float('inf'), [], 0
	for ratio, w, q in workers:
		heapq.heappush(team, -q)
		sumq += q
		if len(team) > K: sumq += heapq.heappop(team)
		if len(team) == K: cost = min(cost, sumq * ratio)
	return cost