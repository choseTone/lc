__author__ = 'wangqc'

# https://leetcode.com/problems/loud-and-rich/discuss/266859/Python-Cached-DFS

import collections

def loudAndRich(richer, quiet):
	g, loud = collections.defaultdict(set), [-1]*len(quiet)
	for u, v in richer: g[v].add(u)
	def dfs(node):
		if loud[node] < 0: loud[node] = min([dfs(nei) for nei in g[node]]+[node], key=lambda x:quiet[x])
		return loud[node]
	return list(map(dfs, range(len(quiet))))