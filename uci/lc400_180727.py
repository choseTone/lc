__author__ = 'wangqc'

'''
400. Nth Digit

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:
Input:
3
Output:
3

Example 2:
Input:
11
Output:
0
Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number
'''


class Solution:
    # 9 one-digit number, 90 two-digit number, 900 three-digit number...
    def findNthDigit(self, n):
        n -= 1
        for d in range(1, 11):
            level = 9 * 10 ** (d-1) * d
            if n < level:
                return int(str(10 ** (d-1) + n // d)[n % d])
            n -= level






if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.findNthDigit(217)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
