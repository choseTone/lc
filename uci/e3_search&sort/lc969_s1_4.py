__author__ = 'wangqc'

# https://leetcode.com/problems/pancake-sorting/discuss/262329/Python-Keeping-Updaing-Kth-Smallest

def pancakeSort(A):
	b = n = len(A)
	ans = []
	for _ in range(n):
		p = A.index(b) + 1
		if p != b:
			ans += [p, b] if p > 1 else [b]
			A = A[p:b][::-1] + A[:p] + A[b:]
		b -= 1
	return ans