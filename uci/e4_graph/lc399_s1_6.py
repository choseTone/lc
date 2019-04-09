__author__ = 'wangqc'

# https://leetcode.com/problems/evaluate-division/discuss/270993/Python-BFS-and-UF(detailed-explanation)

import collections

def calcEquation(equations, values, queries):
	g = collections.defaultdict(set)
	for (x, y), v in zip(equations, values):
		g[x].add((y, v))
		g[y].add((x, 1/v))
	def bfs(src, dst):
		if not (src in g and dst in g): return -1.0
		q, seen = [(src, 1.0)], set()
		for x, v in q:
			if x == dst: return v
			seen.add(x)
			for y, k in g[x]:
				if y not in seen: q.append((y, v*k))
		return -1.0
	return [bfs(s, d) for s, d in queries]

def calcEquationUF(equations, values, queries):
	root = {}
	def find(x):
		p, v = root.setdefault(x, (x, 1.0))
		if x != p:
			r, vp = find(p)
			root[x] = (r, vp*v)
		return root[x]
	for (x, y), v in zip(equations, values):
		(px, vx), (py, vy) = find(x), find(y)
		if px != py: root[px] = (py, vy*v/vx)
	def q(x, y):
		if not (x in root and y in root): return -1.0
		(px, vx), (py, vy) = find(x), find(y)
		return vx / vy if px == py else -1.0
	return [q(x, y) for x, y in queries]
