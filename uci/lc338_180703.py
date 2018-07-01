__author__ = 'wangqc'

from time import time

'''
338. Counting Bits

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 
1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:
It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear 
time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function.
'''

class Solution:
    # bit counts of each element of [2^k, 2^(k+1)-1] are bit counts of each one of [0, 2^k-1] plus 1 (at MSB)
    def countBits(self, num):
        ans = [0]
        while num >= len(ans):
            ans += [i+1 for i in ans]
        return ans[:num+1]

    # not include [num+1, 2^M-1] in the ans, M = log2(num) + 1
    def countBits_tight(self, num):
        if not num: return [0]
        ans, power, tmp = [0], -1, num
        # round = log2(num)
        while tmp:
            tmp >>= 1
            power += 1
        for _ in range(power):
            ans += [i+1 for i in ans]
        rest = num - (1 << power) + 1
        return ans + [i+1 for i in ans[:rest]]

    # update one element each loop, i's top (n-1) bit counts are those of i >> 1, the least significant bit is (i&1)
    def countBits_unit(self, num):
        ans = [0]
        for i in range(1, num + 1):
            ans.append(ans[i >> 1] + (i & 1))
        return ans

if __name__ == '__main__':
    sol = Solution()
    t1 = time()
    ans1 = sol.countBits(2**15)
    t2 = time()
    ans2 = sol.countBits_tight(2**15)
    t3 = time()
    ans3 = sol.countBits_unit(2**15)
    t4 = time()
    # sol1 time: 2.71ms; sol2 time: 1.31ms; sol3 time: 5.17ms
    print('sol1 ans: %s\ntime: %.3fms\n' % (ans1, ((t2 - t1)) * 1000))
    print('sol2 ans: %s\ntime: %.3fms\n' % (ans2, ((t3 - t2)) * 1000))
    print('sol3 ans: %s\ntime: %.3fms' % (ans3, ((t4 - t3)) * 1000))