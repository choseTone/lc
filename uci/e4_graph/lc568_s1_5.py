__author__ = 'wangqc'

# https://leetcode.com/problems/graph-valid-tree/discuss/269173/python-bfs-uf

def validTree(n, edges):
	if len(edges) != n-1: return False
	g, q = {i:[] for i in range(n)}, [0]
	for u, v in edges:
		g[u].append(v), g[v].append(u)
	for x in q:
		q += g.pop(x, [])
	return not g

def validTreeUF(n, edges):
	if len(edges) != n-1: return False
	p = list(range(n))
	def find(x):
		if p[x] != x: p[x] = find(p[x])
		return p[x]
	for x, y in edges:
		px, py = find(x), find(y)
		if px == py: return False
		p[px] = py
	return True