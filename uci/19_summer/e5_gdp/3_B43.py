__author__ = 'wangqc'

# https://leetcode.com/problems/longest-common-subsequence/


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        # dp[i+1][j+1] = dp[i][j] + 1 if t1[i]==t2[j] else max(dp[i+1][j], dp[i][j+1])
        M, N = len(text1), len(text2)
        if M < N:
            M, N, text1, text2 = N, M, text2, text1
        curr = [0]*(N+1)
        for i in range(M):
            prev, curr = curr, [0]*(N+1)
            for j in range(N):
                curr[j+1] = prev[j]+1 if text1[i]==text2[j] else max(curr[j], prev[j+1])
        return curr[N]


if __name__ == '__main__':
    sol = Solution()

    t1 = "abcde", "ace",
    print(sol.longestCommonSubsequence(*t1))

    t2 = "abc", "abc",
    print(sol.longestCommonSubsequence(*t2))

    t3 = "abc", "def",
    print(sol.longestCommonSubsequence(*t3))