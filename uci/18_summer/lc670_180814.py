__author__ = 'wangqc'

'''
670. Maximum Swap

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum 
valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 10^8]
'''


class Solution:
    def maximumSwap(self, num):
        pos, digits = [0] * 10, [int(d) for d in str(num)]
        for i, d in enumerate(digits):
            pos[d] = i
        n = len(digits)
        for i in range(n):
            for p in pos[:digits[i]:-1]:
                if p > i:
                    digits[i], digits[p] = digits[p], digits[i]
                    return sum(d * 10 ** (n-j-1) for j, d in enumerate(digits))
        return num

if __name__ == '__main__':
    from time import time
    from random import randint

    sol = Solution()
    num = randint(1, 100000)

    t = time()
    ans = sol.maximumSwap(num)
    print('num: %s\nans: %s\ntime: %.3fms' % (num, ans, ((time() - t)) * 1000))

