__author__ = 'wangqc'

'''
51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a 
queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''


class Solution:
    def solveNQueens(self, n):
        self.places = []
        self.valid_place([], n)
        return [['.' * col + 'Q' + '.' * (n - col - 1) for col in place] for place in self.places]

    # place one queen row by row(outer loop);
    # check the validation against previous rows' queen's position(col) in terms of not in same col and not in the same
    # diagonal(row_cur - row_prev != abs(col_cur - col_prev)); there is no need to check same row invalidation since
    # only one queen will be placed in one row;
    # decline the invalid position(col) in each row(inner loop), if not valid for all positions(cols) in the row,
    # go back to the previous row and replace the previous queen
    def valid_place(self, place, n, cur_row=0):
        if cur_row == n:
            self.places.append(place[:])
            return
        for col in range(n):    # check validation for each col in the current row
            place.append(col)
            valid = True
            for row in range(cur_row):      # inner loop
                if place[row] == col or abs(col - place[row]) == cur_row - row:
                    valid = False
                    break
            if valid:
                self.valid_place(place, n, cur_row + 1)     # outer loop
            place.pop()


if __name__ == '__main__':
    from time import time

    sol = Solution()
    n = 8
    t = time()
    ans = sol.solveNQueens(n)
    print('time: %.3fms' % (((time() - t)) * 1000))
    for i, place in enumerate(ans):
        print('place %d:' % (i + 1))
        for row in place:
            print(row)
        print('-' * n)
