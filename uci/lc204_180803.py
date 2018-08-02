__author__ = 'wangqc'

'''
204. Count Primes

Count the number of prime numbers less than a non-negative number, n.

Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''


class Solution:
    def countPrimes(self, n):
        if n < 3: return 0
        primes = [0, 0] + [1] * (n-2)
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i*i:n:i] = [0] * len(primes[i*i:n:i])
        return sum(primes)


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.countPrimes(10)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
