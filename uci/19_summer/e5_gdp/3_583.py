__author__ = 'wangqc'

# https://leetcode.com/problems/delete-operation-for-two-strings/


class Solution:
    def minDistance(self, word1, word2):
        # dp[i+1][j+1] = dp[i][j] if w1[i]==w2[j] else min(dp[i+1][j],dp[i][j+1]) + 1
        M, N = len(word1), len(word2)
        if M < N:
            M, N, word1, word2 = N, M, word2, word1
        curr = list(range(N+1))
        for i in range(M):
            prev, curr = curr, [i+1]+[0]*N
            for j in range(N):
                curr[j+1] = prev[j] if word1[i]==word2[j] else min(curr[j], prev[j+1]) + 1
        return curr[N]


if __name__ == '__main__':
    sol = Solution()

    t1 = "sea", "eat",
    print(sol.minDistance(*t1))