__author__ = 'wangqc'

# https://leetcode.com/problems/minimum-window-subsequence/


class Solution:
    def minWindow(self, S, T):
        M, N, left, right = len(S), len(T), -1, float('inf')
        i = j = 0
        while i < M:
            j += (S[i]==T[j])
            if j == N:
                k, j = i+1, j-1
                while j >= 0:
                    j -= (S[i]==T[j])
                    i -= 1
                i, j = i+1, j+1
                left, right = min(((left, right), (i, k)), key=lambda x:x[1]-x[0])
            i += 1
        return S[left: right] if left >= 0 else ""


if __name__ == '__main__':
    sol = Solution()

    t1 = "abcdebdde", "bde",
    print(sol.minWindow(*t1))