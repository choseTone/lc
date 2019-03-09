__author__ = 'wangqc'

'''
289. Game of Life

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by 
the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight 
neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is 
created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur 
simultaneously.

Example:
Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]

Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

Follow up:
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells 
first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause 
problems when the active area encroaches the border of the array. How would you address these problems?
'''


class Solution:
    # in-place solution:
    # store both current(on least significant bit) and next(on 2nd least significant bits) status in one cell's value
    def gameOfLife(self, board):
        if not board: return []
        m, n = len(board), len(board[0])
        for i in range(m):
            t, b = max(0, i-1), min(m, i+2)
            for j in range(n):
                l, r = max(0, j-1), min(n, j+2)
                count = sum(board[y][x] & 1 for y in range(t, b) for x in range(l, r)) - board[i][j] # neighbor sum
                if count | board[i][j] == 3:
                    board[i][j] |= 2
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1



if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()

    board = [
      [0,1,0],
      [0,0,1],
      [1,1,1],
      [0,0,0]
    ]
    sol.gameOfLife(board)
    print('ans: %s\ntime: %.3fms' % (board, ((time() - t)) * 1000))
