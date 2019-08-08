__author__ = 'wangqc'
# https://leetcode.com/problems/minimum-window-substring/

import collections


class Solution:
    def minWindow(self, s, t):
        counter, gap = collections.Counter(t), len(t)
        i, l, r = 0, 0, len(s)+1
        for j, c in enumerate(s, 1):
            gap -= counter[c] > 0
            counter[c] -= 1
            if not gap:
                while i < j and counter[s[i]] < 0:
                    counter[s[i]] += 1
                    i += 1
                if j-i < r-l:
                    l, r = i, j
        return s[l:r] if r <= len(s) else ""


if __name__ == '__main__':

    sol = Solution()

    t1 = "ADOBECODEBANC", "ABC"
    print(sol.minWindow(*t1))

    t2 = "ABCDE", "ABCDE"
    print(sol.minWindow(*t2))

    t3 = "ABCDE", "ABF"
    print(sol.minWindow(*t3))

