__author__ = 'wangqc'

'''
415. Add Strings

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution:
    def addStrings(self, num1, num2):
        if len(num1) < len(num2): num1, num2 = num2, num1
        ans, carry, n = '', 0, len(num1)
        num2 = '0' * (n-len(num2)) + num2
        for i in range(n)[::-1]:
            carry, curr = divmod(int(num1[i]) + int(num2[i]) + carry, 10)
            ans = str(curr) + ans
        return ['', '1'][carry] + ans


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.addStrings('106', '815')
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
