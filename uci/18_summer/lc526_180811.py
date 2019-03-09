__author__ = 'wangqc'

'''
526. Beautiful Arrangement

Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by 
these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.

Now given N, how many beautiful arrangements can you construct?

Example 1:
Input: 2
Output: 2

Explanation: 
The first beautiful arrangement is [1, 2]:
Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
The second beautiful arrangement is [2, 1]:
Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.

Note:
N is a positive integer and will not exceed 15.
'''


class Solution():
    cache = {}
    def countArrangement(self, N):
        return self.counter(N, tuple(range(1, N+1)))

    def counter(self, i, X):
        if i == 1: return 1
        key = (i, X)
        if key in self.cache: return self.cache[key]
        count = sum(self.counter(i - 1, X[:j] + X[j+1:]) for j, x in enumerate(X) if not (i % x and x % i))
        self.cache[key] = count
        return count

if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    ans = sol.countArrangement(10)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

