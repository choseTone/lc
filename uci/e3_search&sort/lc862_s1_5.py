__author__ = 'wangqc'

# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/262641/Python-Prefix-Sum-and-Sliding-Window

import collections

def shortestSubarray(A, K):
	n = len(A)
	q, ans, psum = collections.deque([(-1,0)]), n+1, 0
	for i, a in enumerate(A):
		psum += a
		if a > 0:
			while q and psum - q[0][1] >= K:
				ans = min(ans, i-q.popleft()[0])
		else:
			while q and psum <= q[-1][1]:
				q.pop()
		q.append((i, psum))
	return ans if ans <= n else -1