__author__ = 'wangqc'

# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/discuss/266228/python-dfsbfsuf

import collections

def countComponents(n, edges):
	g, cnt, seen = collections.defaultdict(set), 0, set()
	for u, v in edges:
		g[u].add(v), g[v].add(u)

	def dfs(node):
		if node not in seen:
			seen.add(node)
			for nei in g[node]: dfs(nei)
		return 1

	def bfs(q):
		for node in q:
			if node not in seen:
				q += g[node]
				seen.add(node)
		return 1

	# return sum(dfs(i) for i in range(n) if i not in seen)
	return sum(bfs([i]) for i in range(n) if i not in seen)

def countComponentsUF(n, edges):
	p = list(range(n))
	def find(x):
		if x != p[x]: p[x] = find(p[x])
		return p[x]
	for u, v in edges:
		p[find(u)] = find(v)
	return len(set(map(find, range(n))))