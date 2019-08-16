__author__ = 'wangqc'


# https://leetcode.com/problems/unique-letter-string/


class Solution:
    def uniqueLetterString(self, S):
        M, N, cnt = 10**9+7, len(S), 0
        dp = {c:(-1,-1) for c in set(S)}
        for r, c in enumerate(S):
            l, m = dp[c]
            cnt = (cnt + (m-l)*(r-m)) % M
            dp[c] = (m, r)
        return cnt + sum((dp[c][1]-dp[c][0]) * (N-dp[c][1]) % M for c in dp) % M




if __name__ == '__main__':
    sol = Solution()

    t1 = "PANAMABANANA",
    print(sol.uniqueLetterString(*t1))

    t2 = "QWERTYUIOPASDFGHJKLZXCVBNM",
    print(sol.uniqueLetterString(*t2))
