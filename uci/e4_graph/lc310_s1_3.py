__author__ = 'wangqc'

# https://leetcode.com/problems/word-ladder-ii/discuss/269012/python-bfsbacktrack-greatly-improved-by-directional-bfs

import collections

def findLadders(beginWord, endWord, wordList):
	tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
	if endWord not in wordList: return []
	found, bq, eq, nq, rev = False, {beginWord}, {endWord}, set(), False
	while bq and not found:
		words -= set(bq)
		for x in bq:
			for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in 'abcdefghijklmnopqrstuvwxyz']:
				if y in words:
					if y in eq: found = True
					else: nq.add(y)
					tree[y].add(x) if rev else tree[x].add(y)
		bq, nq = nq, set()
		if len(bq) > len(eq): bq, eq, rev = eq, bq, not rev
	def bt(x): return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]
	return bt(beginWord)