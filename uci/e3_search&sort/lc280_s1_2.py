__author__ = 'wangqc'

# https://leetcode.com/problems/find-peak-element/discuss/258772/Python-Binary-Search

def wiggleSort(nums):
	for i in range(len(nums)-1):
		if (i & 1) == (nums[i] < nums[i+1]):
			nums[i], nums[i+1] = nums[i+1], nums[i]