__author__ = 'wangqc'

# https://leetcode.com/problems/battleships-in-a-board/discuss/266462/python-one-pass-constant-space-just-count-top-left-corner-x

def countBattleships(board):
	m, n = len(board), len(board) and len(board[0])
	return sum(1 for i in range(m) for j in range(n)
			   if board[i][j]=='X' and (not i or board[i-1][j]=='.') and (not j or board[i][j-1]=='.'))