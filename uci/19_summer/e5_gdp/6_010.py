__author__ = 'wangqc'

# https://leetcode.com/problems/regular-expression-matching/


class Solution:
    def isMatch(self, s, p):
        M, N = len(s), len(p)
        curr = [False]*N + [True]
        for i in range(N-2,-1,-1):
            curr[i] = p[i+1]=="*" and curr[i+2]
        for c in s[::-1]:
            prev, curr = curr, [False]*(N+1)
            for i in range(N-1,-1,-1):
                if i<N-1 and p[i+1]=="*":
                    curr[i] = curr[i+2] or p[i] in {c, "."} and prev[i]
                else:
                    curr[i] = p[i] in {c, "."} and prev[i+1]
        return curr[0]


if __name__ == '__main__':
    sol = Solution()

    t1 = "ab", ".*"
    print(sol.isMatch(*t1))

    t2 = "aab", "c*a*b"
    print(sol.isMatch(*t2))

    t3 = "mississippi", "mis*is*p*."
    print(sol.isMatch(*t3))