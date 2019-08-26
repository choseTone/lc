__author__ = 'wangqc'


# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter

class Solution:
    def minWindow(self, S, T):
        counter, gap = Counter(T), len(T)
        i, l, r = 0, 0, len(S)+1
        for j, c in enumerate(S, 1):
            gap -= counter[c] > 0
            counter[c] -= 1
            if not gap:
                while counter[S[i]] < 0:
                    counter[S[i]] += 1
                    i += 1
                if j-i < r-l:
                    l, r = i, j
        return S[l:r] if r <= len(S) else ""


if __name__ == '__main__':
    sol = Solution()

    t1 = "ADOBECODEBANC", "ABC"
    print(sol.minWindow(*t1))
