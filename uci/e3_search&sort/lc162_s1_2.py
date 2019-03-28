__author__ = 'wangqc'

# https://leetcode.com/problems/find-peak-element/discuss/258772/Python-Binary-Search

def findPeakElement(nums):
	lo, hi = 0, len(nums) - 1
	while lo < hi:
		mid = lo + hi >> 1
		if nums[mid] > nums[mid+1]: hi = mid
		else: lo = mid + 1
	return lo