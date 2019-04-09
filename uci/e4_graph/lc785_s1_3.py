__author__ = 'wangqc'

# https://leetcode.com/problems/is-graph-bipartite/discuss/269084/python-concise-dfs

def isBipartite(graph):
	group = {}
	def dfs(x, g):
		if x in group:
			return g == group[x]
		group[x] = g
		return all(dfs(y, 1-g) for y in graph[x])
	return all(dfs(x, 0) for x in range(len(graph)) if x not in group)