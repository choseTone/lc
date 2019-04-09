__author__ = 'wangqc'

# https://leetcode.com/problems/k-similar-strings/discuss/269517/Python-Graph-BFS

def kSimilarity(A, B):
	def nei(x):
		i = 0
		while x[i] == B[i]: i+=1
		for j in range(i+1, len(x)):
			if x[j] == B[i]: yield x[:i]+x[j]+x[i+1:j]+x[i]+x[j+1:]
	q, seen = [(A,0)], {A}
	for x, d in q:
		if x == B: return d
		for y in nei(x):
			if y not in seen:
				seen.add(y), q.append((y,d+1))