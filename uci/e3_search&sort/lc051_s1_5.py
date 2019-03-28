__author__ = 'wangqc'

# https://leetcode.com/problems/n-queens/discuss/262826/Python-DFS

def solveNQueens(n):
	def dfs(state, pd, nd):
		r = len(state)
		if r != n:
			for c in range(n):
				if c not in state and c-r not in pd and c+r not in nd:
					dfs(state+[c], pd|{c-r}, nd|{c+r})
		else: sols.append(state)
	sols = []
	dfs([], set(), set())
	return [['.'*c+'Q'+'.'*(n-c-1) for c in sol] for sol in sols]