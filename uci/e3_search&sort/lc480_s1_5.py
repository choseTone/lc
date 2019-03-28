__author__ = 'wangqc'

# https://leetcode.com/problems/sliding-window-median/discuss/262689/Python-Small-and-Large-Heaps

import heapq

def medianSlidingWindow(nums, k):
	small, large, ans = [], [], []
	for i, n in enumerate(nums[:k]):
		heapq.heappush(small, (-n,i))
	for _ in range(k-(k>>1)):
		move(small, large)
	ans = [large[0][0] * 1. if k & 1 else (large[0][0]-small[0][0]) / 2.]
	for i, n in enumerate(nums[k:]):
		if n >= large[0][0]:
			heapq.heappush(large, (n, i+k))
			if nums[i] <= large[0][0]: move(large, small)
		else:
			heapq.heappush(small, (-n, i+k))
			if nums[i] >= large[0][0]: move(small, large)
		while small and small[0][1] <= i: heapq.heappop(small)
		while large and large[0][1] <= i: heapq.heappop(large)
		ans.append(large[0][0] * 1. if k & 1 else (large[0][0]-small[0][0]) / 2.)
	return ans

def move(h1, h2):
	x, i = heapq.heappop(h1)
	heapq.heappush(h2, (-x, i))