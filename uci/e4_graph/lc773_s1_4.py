__author__ = 'wangqc'

# https://leetcode.com/problems/word-search-ii/discuss/269110/python-clean-trie-dfs

def findWords(board, words):
	trie, ans, m, n = {}, set(), len(board), len(board) and len(board[0])
	for word in words:
		node = trie
		for c in word: node = node.setdefault(c, {})
		node['$'] = None
	def dfs(i, j, node, word):
		if board[i][j] in node:
			board[i][j], c = '', board[i][j]
			node, word = node[c], word + c
			if '$' in node: ans.add(word)
			for x, y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
				if 0 <= x < m and 0 <= y < n:
					dfs(x, y, node, word)
			board[i][j] = c
	for i in range(m):
		for j in range(n):
			dfs(i, j, trie, '')
	return list(ans)