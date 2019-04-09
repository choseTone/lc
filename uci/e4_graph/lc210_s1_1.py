__author__ = 'wangqc'

# https://leetcode.com/problems/course-schedule-ii/discuss/266867/Python-10-Lines-Topological-Sort

def findOrder(n, prerequisites):
	src, dst = [set() for _ in range(n)], [set() for _ in range(n)]
	for d, s in prerequisites:
		src[d].add(s), dst[s].add(d)
	ans = [x for x in range(n) if not src[x]]
	for s in ans:
		for d in dst[s]:
			src[d].remove(s)
			if not src[d]: ans.append(d)
	return ans if len(ans) == n else []