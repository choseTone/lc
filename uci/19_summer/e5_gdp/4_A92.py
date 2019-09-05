__author__ = 'wangqc'

# https://leetcode.com/problems/shortest-common-supersequence/


from functools import lru_cache

class Solution:
    def shortestCommonSupersequence(self, str1, str2):
        M, N = len(str1), len(str2)
        dp = [list(range(N+1))] + [[i]+[0]*N for i in range(1, M+1)]
        for i in range(M):
            for j in range(N):
                dp[i+1][j+1] = 1 + (dp[i][j] if str1[i]==str2[j] else min(dp[i+1][j], dp[i][j+1]))
        i, j, scs = M, N, ""
        while i * j:
            c1, c2 = str1[i-1], str2[j-1]
            equal, c1_in, c2_in = c1==c2, dp[i][j-1] > dp[i-1][j], dp[i][j-1] <= dp[i-1][j]
            scs = c1 + scs if equal or c1_in else c2 + scs
            i -= int(equal or c1_in)
            j -= int(equal or c2_in)
        return str1[:i] + str2[:j] + scs


if __name__ == '__main__':
    sol = Solution()

    t1 = "abac", "cab",
    print(sol.shortestCommonSupersequence(*t1))

    t2 = "bbbaaaba", "bbababbb",
    print(sol.shortestCommonSupersequence(*t2))

