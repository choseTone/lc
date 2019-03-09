__author__ = 'wangqc'

'''
212. Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally 
or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]
Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''


class Solution:
    # use trie structure to save the repeat search; use '$' as the end mark of a word
    def findWords(self, board, words):
        if not board: return False
        m, n, ans = len(board), len(board[0]), set()
        trie = {}
        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node['$'] = None

        def search(i, j, node, prefix):
            if board[i][j] in node:
                board[i][j], cur = None, board[i][j]
                node, prefix = node[cur], prefix + cur
                if '$' in node: ans.add(prefix)
                if j > 0: search(i, j-1, node, prefix)
                if j < n-1: search(i, j+1, node, prefix)
                if i > 0: search(i-1, j, node, prefix)
                if i < m-1: search(i+1, j, node, prefix)
                board[i][j] = cur

        for i in range(m):
            for j in range(n):
                search(i, j, trie, '')
        return list(ans)


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    board = [['o', 'a', 'a', 'n'],
             ['e', 't', 'a', 'e'],
             ['i', 'h', 'k', 'r'],
             ['i', 'f', 'l', 'v']]
    ans = sol.findWords(board, ["oath","pea","eat","rain"])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))