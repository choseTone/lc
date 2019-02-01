__author__ = 'wangqc'

'''
782. Transform to Chessboard

An N x N board contains only 0s and 1s. In each move, you can swap any 2 rows with each other, or any 2 columns with each other.
What is the minimum number of moves to transform the board into a "chessboard" - a board where no 0s and no 1s are 
4-directionally adjacent? If the task is impossible, return -1.

Examples:

Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
Output: 2
Explanation:
One potential sequence of moves is shown below, from left to right:
0110     1010     1010
0110 --> 1010 --> 0101
1001     0101     1010
1001     0101     0101
The first move swaps the first and second column.
The second move swaps the second and third row.

Input: board = [[0, 1], [1, 0]]
Output: 0
Explanation:
Also note that the board with 0 in the top left corner,
01
10
is also a valid chessboard.
Input: board = [[1, 0], [1, 0]]
Output: -1
Explanation:
No matter what sequence of moves you make, you cannot end with a valid chessboard.

Note:
board will have the same number of rows and columns, a number in the range [2, 30].
board[i][j] will be only 0s or 1s.
'''

import collections

class Solution:
    def movesToChessboard(self, board):
        n, ans = len(board), 0
        for count in (collections.Counter(map(tuple, board)), collections.Counter(zip(*board))):
            # only two kinds of line; the same-idx elements should be xor; 0's and 1's counts diff at most 1
            if len(count) != 2 or sorted(count.values()) != [n>>1, n+1>>1]: return -1
            l1, l2 = count
            if not all(x ^ y for x, y in zip(l1, l2)): return -1
            # if len is odd, only one possible line that starts with the majority, otherwise two possible lines
            starts = [+(l1.count(1)<<1 > n)] if n&1 else [0,1]
            ans += min(sum(i&1^x for i, x in enumerate(l1, start)) for start in starts) >> 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    argv = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
    ans = sol.movesToChessboard(argv)
    print('Input : %s\nOutput: %s' % (argv, ans))

