__author__ = 'wangqc'

import time

'''
119. Pascal's Triangle II
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.

Example:
Input: 3
Output: [1,3,3,1]

Follow up:
Could you optimize your algorithm to use only O(k) extra space?
'''

class Solution:
    # simple list comprehension
    def getRow(self, rowIndex):
        res = [1]
        for _ in range(rowIndex):
            res = [1] + [res[i-1]+res[i] for i in range(1, len(res))] + [1]
        return res


if __name__ == '__main__':
    sol = Solution()
    t = time.time()
    ans = sol.getRow(12)
    print('ans: %s\ntime: %.2fms' % (ans, ((time.time() - t)) * 1000))