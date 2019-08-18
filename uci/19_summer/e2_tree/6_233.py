__author__ = 'wangqc'


# https://leetcode.com/problems/number-of-digit-one/


class Solution:
    def countDigitOne(self, n):
        N = len(str(n))
        return sum((n//m+8)//10*m + (n//m%10==1)*(n%m+1) for m in (10**i for i in range(N)))


if __name__ == '__main__':
    sol = Solution()

    t1 = 371,
    print(sol.countDigitOne(*t1))

    t2 = 27315,
    print(sol.countDigitOne(*t2))
