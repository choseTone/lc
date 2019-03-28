__author__ = 'wangqc'

# https://leetcode.com/problems/3sum-closest/discuss/263269/Python-N2-Two-Pointers

def threeSumClosest(nums, target):
	nums.sort()
	cand, n = set(), len(nums)
	for i in range(n-2):
		head, l, r, best = nums[i], i+1, n-1, float('inf')
		small, large =  head+nums[l]+nums[l+1], head+nums[r-1]+nums[r]
		if small > target: cand.add(small)
		elif large < target: cand.add(large)
		else:
			while l < r:
				gap = target-head-nums[l]-nums[r]
				if gap > 0: l += 1
				elif gap < 0: r -= 1
				else: return target
				best = min(best, gap, key=abs)
			cand.add(target-best)
	return min(cand, key=lambda x:abs(x-target))