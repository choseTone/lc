__author__ = 'wangqc'


# https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board, click):
        i, j, M, N = *click, len(board), len(board[0])
        def dfs(i, j):
            if board[i][j] == "E":
                neis = [(x, y)
                        for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1))
                        if 0<=x<M and 0<=y<N]
                cnt = sum(board[x][y]=="M" for x, y in neis)
                if not cnt:
                    board[i][j] = "B"
                    for x, y in neis:
                        dfs(x, y)
                else:
                    board[i][j] = str(cnt)
        if board[i][j] == "M":
            board[i][j] = "X"
        else:
            dfs(i, j)
        return board


if __name__ == '__main__':
    sol = Solution()

    t1 = [
             ['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E']
         ], [3,0],
    print(sol.updateBoard(*t1))

    t2 = [
             ['B', '1', 'E', '1', 'B'],
             ['B', '1', 'M', '1', 'B'],
             ['B', '1', '1', '1', 'B'],
             ['B', 'B', 'B', 'B', 'B']
         ], [1,2],
    print(sol.updateBoard(*t2))

