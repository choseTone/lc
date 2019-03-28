__author__ = 'wangqc'

# https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/262929/Python-Binary-Search-O(log(min(m-n)))

def findMedianSortedArrays(A, B):
	l1, l2 = len(A), len(B)
	if l1 > l2: l1, l2, A, B = l2, l1, B, A
	l, r = 0, l1
	while l <= r:
		i = l + r >> 1
		j = (l1 + l2 + 1 >> 1) - i
		if i > 0 and A[i-1] > B[j]: r = i-1
		elif i < l1 and A[i] < B[j-1]: l = i+1
		else:
			left = max(A[i-1], B[j-1]) if i*j else B[j-1] if j else A[i-1]
			if l1 + l2 & 1: return left / 1.
			right = B[j] if i==l1 else A[i] if j==l2 else min(A[i], B[j])
			return (left + right) / 2.