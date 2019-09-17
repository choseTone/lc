__author__ = 'wangqc'

# https://leetcode.com/problems/unique-letter-string/


class Solution:
    def uniqueLetterString(self, S):
        M, N, cnt = 10**9 + 7, len(S), 0
        dp = {c:(-1, -1) for c in set(S)}
        for k, c in enumerate(S):
            i, j = dp[c]
            cnt = (cnt + (k-j)*(j-i)) % M
            dp[c] = (j, k)
        return (cnt + sum((N-j)*(j-i) for i, j in dp.values())) % M


if __name__ == '__main__':
    sol = Solution()

    t1 = "ABC",
    print(sol.uniqueLetterString(*t1))

    t2 = "ABA",
    print(sol.uniqueLetterString(*t2))