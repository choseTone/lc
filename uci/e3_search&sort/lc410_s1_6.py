__author__ = 'wangqc'

# https://leetcode.com/problems/split-array-largest-sum/discuss/263297/Python-Binary-Search

def splitArray(nums, m):
	lo, hi = max(nums), sum(nums)
	while lo < hi:
		mid, val, cnt = lo+hi>>1, 0, 1
		for n in nums:
			val += n
			if val > mid: cnt, val = cnt + 1, n
			if cnt > m: break
		if cnt > m: lo = mid+1
		else: hi = mid
	return lo