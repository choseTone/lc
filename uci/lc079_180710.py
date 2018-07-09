__author__ = 'wangqc'

'''
79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally 
or vertically neighboring. The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''


class Solution:
    def exist(self, board, word):
        if not board: return False
        m, n = len(board), len(board[0])

        def search(i, j, cur):
            if not cur: return True
            if 0 <= i < m and 0 <= j < n and cur[0] == board[i][j]:
                board[i][j], nex = None, cur[1:]
                match = search(i-1, j, nex) or search(i+1, j, nex) or search(i, j-1, nex) or search(i, j+1, nex)
                board[i][j] = cur[0]
                return match
            return False

        return any(search(i, j, word) for i in range(m) for j in range(n))


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    board = [['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']]
    ans = sol.exist(board, "ABCCED")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))