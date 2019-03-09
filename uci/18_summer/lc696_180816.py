__author__ = 'wangqc'

'''
696. Count Binary Substrings

Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all 
the 0's and all the 1's in these substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

Note:
s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
'''


class Solution:
    def countBinarySubstrings(self, s):
        seg = list(map(len, s.replace("01", "0 1").replace("10", "1 0").split()))
        return sum(min(a, b) for a, b in zip(seg, seg[1:]))


if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    ans = sol.countBinarySubstrings("0000111001111100")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

