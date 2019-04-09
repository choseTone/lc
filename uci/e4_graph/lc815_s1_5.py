__author__ = 'wangqc'

# https://leetcode.com/problems/bus-routes/discuss/269514/Python-Graph-BFS

def numBusesToDestination(routes, S, T):
	if S == T: return 0
	routes, n = [set(r) for r in routes], len(routes)
	g = [set() for _ in range(n)]
	for i in range(n):
		for j in range(i):
			if set(routes[i]) & set(routes[j]):
				g[i].add(j), g[j].add(i)
	seen, dst = set(i for i,r in enumerate(routes) if S in r), set(i for i,r in enumerate(routes) if T in r)
	q = [(x, 1) for x in seen]
	for x, d in q:
		if x in dst: return d
		for y in g[x]:
			if y not in seen: seen.add(y), q.append((y, d+1))
	return -1