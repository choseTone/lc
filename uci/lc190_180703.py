__author__ = 'wangqc'

from time import time

'''
190. Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

Example:
Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
             return 964176192 represented in binary as 00111001011110000010100101000000.
Follow up:
If this function is called many times, how would you optimize it?
'''

class Solution:
    # use basic bit operations and mask techniques
    def reverseBits(self, n):
        mask_8, mask_4, mask_2, mask_1 = 0xff00ff, 0xf0f0f0f, 0x33333333, 0x55555555
        n = n << 16 | n >> 16
        n = (n & mask_8) << 8 | (n >> 8) & mask_8
        n = (n & mask_4) << 4 | (n >> 4) & mask_4
        n = (n & mask_2) << 2 | (n >> 2) & mask_2
        return (n & mask_1) << 1 | (n >> 1) & mask_1

if __name__ == '__main__':
    sol = Solution()
    n = 2 ** 31 + 43261597
    t = time()
    ans = sol.reverseBits(n)
    # before: 0b10000010100101000001111010011101
    # after : 0b10111001011110000010100101000001
    print('before: %s\nafter : %s\nans: %s\ntime: %.3fms' % (bin(n), bin(ans), ans, ((time() - t)) * 1000))