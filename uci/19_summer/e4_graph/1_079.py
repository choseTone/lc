__author__ = 'wangqc'


# https://leetcode.com/problems/word-search/

from collections import Counter

class Solution:
    def exist(self, board, word):
        counter = Counter(sum(board, []))
        for c, n in Counter(word).items():
            if counter[c] < n:
                return False

        M, N, L = len(board), len(board) and len(board[0]), len(word)
        def dfs(x, y, i):
            if i == L:
                return True
            if 0 <= x < M and 0 <= y < N and board[x][y] == word[i]:
                board[x][y] = ""
                match = dfs(x-1,y,i+1) or dfs(x+1,y,i+1) or dfs(x,y-1,i+1) or dfs(x,y+1,i+1)
                board[x][y] = word[i]
                return match
            return False
        for i in range(M):
            for j in range(N):
                if dfs(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    sol = Solution()

    board = [
             ['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']
         ]
    print(sol.exist(board, "ABCCED"))
    print(sol.exist(board, "SEE"))
    print(sol.exist(board, "ABCB"))

