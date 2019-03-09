__author__ = 'wangqc'

'''
67. Add Binary

Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
'''


class Solution:
    def addBinary(self, a, b):
        carry, i, ans = 0, -1, ''
        if len(a) < len(b): a, b = b, a
        b = '0' * (len(a) - len(b)) + b
        for i in range(len(a))[::-1]:
            carry, curr = divmod(int(a[i])+int(b[i])+carry, 2)
            ans = str(curr) + ans
        return str(carry) + ans if carry else ans


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.addBinary("1111", "1")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
