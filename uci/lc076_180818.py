__author__ = 'wangqc'

'''
76. Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''

import collections

class Solution:
    def minWindow(self, s, t):
        words, miss = collections.Counter(t), len(t)
        i = l = r = 0
        for j, c in enumerate(s, 1):
            miss -= words[c] > 0
            words[c] -= 1
            if not miss:
                while i < j and words[s[i]] < 0:
                    words[s[i]] += 1
                    i += 1
                if not r or j - i < r - l:
                    l, r = i, j
        return s[l:r]




if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    ans = sol.minWindow("ADOBECODEBANC", "ABC")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

