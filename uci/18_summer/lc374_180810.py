__author__ = 'wangqc'

'''
374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I'll tell you whether the number is higher or lower.
You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!

Example:
n = 10, I pick 6.

Return 6.
'''

target = 106
def guess(number):
    return -1 if target < number else 1 if target > number else 0

class Solution(object):
    def guessNumber(self, n):
        l, r = 1, n
        while l < r:
            m = (l + r) >> 1
            l, r = [(m, m), (m+1, r), (l, m-1)][guess(m)]
        return l

if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.guessNumber(815)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

