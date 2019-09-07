__author__ = 'wangqc'

# https://leetcode.com/problems/longest-chunked-palindrome-decomposition/


class Solution:
    def longestDecompositionDP(self, text):
        memo = {}

        def dp(l, r):
            if l > r:
                return 0
            if l == r:
                return 1
            if (l, r) not in memo:
                memo[l, r] = max((2 + dp(l+d+1, r-d-1)
                                  for d in range(r-l+1>>1) if text[l:l+d+1]==text[r-d:r+1]),
                                default=1)
            return memo[l, r]

        return dp(0, len(text)-1)

    def longestDecompositionGreedy(self, text):
        k, l, r = 0, "", ""
        for i, j in zip(text, text[::-1]):
            l, r = l + i, j + r
            if l == r:
                k, l, r = k+1, "", ""
        return k


if __name__ == '__main__':
    sol = Solution()

    t1 = "ghiabcdefhelloadamhelloabcdefghi",
    print(sol.longestDecompositionDP(*t1))
    print(sol.longestDecompositionGreedy(*t1))

    t2 = "merchant",
    print(sol.longestDecompositionDP(*t2))
    print(sol.longestDecompositionGreedy(*t2))

    t3 = "antaprezatepzapreanta",
    print(sol.longestDecompositionDP(*t3))
    print(sol.longestDecompositionGreedy(*t3))

    t4 = "aaa",
    print(sol.longestDecompositionDP(*t4))
    print(sol.longestDecompositionGreedy(*t4))