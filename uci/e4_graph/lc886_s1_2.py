__author__ = 'wangqc'

# https://leetcode.com/problems/possible-bipartition/discuss/267265/Python-DFS-for-Bipartite-Problem

import collections

def possibleBipartition(N, dislikes):
	graph, group = collections.defaultdict(set), {}
	for u, v in dislikes: graph[u].add(v), graph[v].add(u)
	def dfs(node, g):
		if node in group: return group[node] == g
		group[node] = g
		return all(dfs(nei, 1-g) for nei in graph[node])
	return all(dfs(node, 0) for node in range(1,N+1) if node not in group)