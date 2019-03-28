__author__ = 'wangqc'

# https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/257587/Python-Priority-Queue-and-Quick-Select

import heapq, random

def findKthLargestHeap(nums, k):
	pq = []
	for x in nums:
		heapq.heappush(pq, x)
		if len(pq) > k: heapq.heappop(pq)
	return heapq.heappop(pq)

def findKthLargestQselect(nums, k):
	if not nums: return
	random.shuffle(nums)
	l, m, r = [x for x in nums if x > nums[0]], [x for x in nums if x == nums[0]], [x for x in nums if x < nums[0]]
	nums, li, ri = l+m+r, len(l), len(l)+len(m)
	return findKthLargestQselect(nums[:li], k) if k <= li else findKthLargestQselect(nums[ri:], k-ri) if k > ri else nums[li]