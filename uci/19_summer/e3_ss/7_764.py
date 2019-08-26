__author__ = 'wangqc'


# https://leetcode.com/problems/largest-plus-sign/

import bisect

class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        rows, cols, sz = [[-1,N] for _ in range(N)], [[-1,N] for _ in range(N)], 0
        for r, c in mines:
            bisect.insort(rows[r], c)
            bisect.insort(cols[c], r)
        for x, row in enumerate(rows):              # x is x-axis of a cross
            for i in range(len(row)-1):             # each i in row has a mine
                l, r = row[i], row[i+1]             # so row region (l,r) is clear
                for y in range(l+sz+1, r-sz):       # y is y-axis of a cross
                    j = bisect.bisect(cols[y], x)   # bisearch one-axis, n^2 -> nlogn
                    t, b = cols[y][j-1], cols[y][j] # t, b are closest mines around cross center cols[y][x]
                    sz = max(sz, min(x-t, b-x, y-l, r-y)) # so col region (b,t) is clear, find smallest radius
        return sz


if __name__ == '__main__':
    sol = Solution()

    t1 = 5, [[4,2]],
    print(sol.orderOfLargestPlusSign(*t1))

    t2 = 1, [[0,0]],
    print(sol.orderOfLargestPlusSign(*t2))
