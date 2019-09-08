__author__ = 'wangqc'

# https://leetcode.com/problems/wildcard-matching/


class Solution:
    def isMatch(self, s, p):
        N = len(s)
        if len(p) - p.count("*") > N:
            return False
        dp = [True] + [False] * N
        for c in p:
            if c == "*":
                for i in range(N):
                    dp[i+1] |= dp[i]
            else:
                for i in range(N-1,-1,-1):
                    dp[i+1] = dp[i] and c in (s[i], "?")
                if dp[0]: dp[0] = False
        return dp[N]


if __name__ == '__main__':
    sol = Solution()

    t1 = "acdcb", "a*d?b"
    print(sol.isMatch(*t1))

    t2 = "acdcb", "a*c?b"
    print(sol.isMatch(*t2))

    t3 = "adceb", "*a*b"
    print(sol.isMatch(*t3))