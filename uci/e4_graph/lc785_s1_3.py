__author__ = 'wangqc'

# https://leetcode.com/problems/minimum-height-trees/discuss/269060/Python-Topological

import collections

def findMinHeightTrees(n, edges):
	tree = [set() for _ in range(n)]
	for u, v in edges: tree[u].add(v), tree[v].add(u)
	q, nq = [x for x in range(n) if len(tree[x]) < 2], []
	while True:
		for x in q:
			for y in tree[x]:
				tree[y].remove(x)
				if len(tree[y]) == 1: nq.append(y)
		if not nq: break
		nq, q = [], nq
	return q