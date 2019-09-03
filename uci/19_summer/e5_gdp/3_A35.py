__author__ = 'wangqc'

# https://leetcode.com/problems/uncrossed-lines/


class Solution:
    def maxUncrossedLines(self, A, B):
        # longest common subsequence
        M, N = len(A), len(B)
        if M < N:
            M, N, A, B = N, M, B, A
        curr = [0] * (N+1)
        for i in range(M):
            prev, curr = curr, [0] * (N+1)
            for j in range(N):
                curr[j+1] = prev[j]+1 if A[i]==B[j] else max(curr[j], prev[j+1])
        return curr[N]


if __name__ == '__main__':
    sol = Solution()

    t1 = [1,4,2], [1,2,4],
    print(sol.maxUncrossedLines(*t1))

    t2 = [2,5,1,2,5], [10,5,2,1,5,2],
    print(sol.maxUncrossedLines(*t2))

    t3 = [1,3,7,1,7,5], [1,9,2,5,1],
    print(sol.maxUncrossedLines(*t3))