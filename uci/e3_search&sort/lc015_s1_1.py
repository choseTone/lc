__author__ = 'wangqc'

# https://leetcode.com/problems/3sum/discuss/257912/Python-Positive-Array-and-Negative-Array-wo-Sort-(Beat-98)

import collections

def threeSum(nums):
	if len(nums) < 3: return []
	counter = collections.Counter(nums)
	tri = [[0,0,0]] if counter[0] > 2 else []
	neg, pos = [x for x in counter if x < 0], [x for x in counter if x >= 0]
	for n in neg:
		for p in pos:
			x = -n-p
			if x in counter:
				if x in {n, p} and counter[x] > 1: tri.append([n,x,p])
				if x < n: tri.append([x,n,p])
				if x > p: tri.append([n,p,x])
	return tri