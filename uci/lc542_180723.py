__author__ = 'wangqc'

'''
542. 01 Matrix

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example 1: 
Input:
0 0 0
0 1 0
0 0 0

Output:
0 0 0
0 1 0
0 0 0

Example 2: 
Input:
0 0 0
0 1 0
1 1 1

Output:
0 0 0
0 1 0
1 2 1

Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
'''


class Solution(object):
    def updateMatrix(self, matrix):
        ans = [[x * 10000 for x in row] for row in matrix]
        for _ in range(4):  # rotate 90 degree 4 times to check all the directions
            for row in ans:
                for j in range(1, len(row)):
                    row[j] = min(row[j], row[j-1] + 1)  # check one direction
            ans = list(map(list, zip(*ans[::-1])))
        return ans



if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()

    matrix = [
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1]
    ]

    ans = sol.updateMatrix(matrix)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
