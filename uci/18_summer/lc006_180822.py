__author__ = 'wangqc'

'''
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display 
this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
'''

class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s): return s
        ans, row, down = [''] * numRows, 0, 1
        for c in s:
            ans[row] += c
            if not row: down = 1
            elif row == numRows - 1: down = -1
            row += down
        return ''.join(ans)


if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    ans = sol.convert("PAYPALISHIRING", 4)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

