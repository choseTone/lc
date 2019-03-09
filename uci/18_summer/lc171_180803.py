__author__ = 'wangqc'

'''
171. Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
    
Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701
'''


class Solution:
    def titleToNumber(self, s):
        return sum(26 ** i * (ord(c) - 64) for i, c in enumerate(s[::-1]))


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.titleToNumber("AB")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
