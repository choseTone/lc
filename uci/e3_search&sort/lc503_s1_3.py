__author__ = 'wangqc'

# https://leetcode.com/problems/next-greater-element-ii/discuss/260393/Python-Two-Pass-Greedy

def nextGreaterElements(nums):
	n = len(nums)
	stack, ans = [], [-1]*n
	def run(first):
		for i, x in enumerate(nums):
			while stack and nums[stack[-1]] < x:
				ans[stack.pop()] = x
			if first: stack.append(i)
	run(True), run(False)
	return ans