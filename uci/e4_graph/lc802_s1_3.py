__author__ = 'wangqc'

# https://leetcode.com/problems/find-eventual-safe-states/discuss/267582/python-dfs

import collections

def eventualSafeNodes(graph):
	check = collections.Counter()
	def dfs(node):
		if check[node]: return check[node] == 2
		check[node] = 1
		for nei in graph[node]:
			if check[nei] == 1 or (not check[nei] and not dfs(nei)): return False
		check[node] = 2
		return True
	return list(filter(dfs, range(len(graph))))