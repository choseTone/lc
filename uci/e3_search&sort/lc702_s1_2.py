__author__ = 'wangqc'

# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/discuss/258535/Python-Binary-Search-How-to-design-for-a-specific-case

def search(reader, target):
	hi = 1
	while reader.get(hi) < target: hi <<= 1
	lo = hi >> 1
	while lo <= hi:
		mid = lo + hi >> 1
		if reader.get(mid) < target: lo = mid + 1
		elif reader.get(mid) > target: hi = mid - 1
		else: return mid
	return -1