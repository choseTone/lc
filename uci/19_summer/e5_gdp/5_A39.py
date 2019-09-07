__author__ = 'wangqc'

# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/


class Solution:
    def minScoreTriangulation(self, A):
        memo = {}

        def dp(i, j):
            if j - i < 2:
                return 0
            if (i, j) not in memo:
                memo[i, j] = min(dp(i,k)+ A[i]*A[k]*A[j] +dp(k,j) for k in range(i+1,j))
            return memo[i, j]

        return dp(0, len(A)-1)


if __name__ == '__main__':
    sol = Solution()

    t1 = [1,2,3],
    print(sol.minScoreTriangulation(*t1))

    t2 = [3,7,4,5],
    print(sol.minScoreTriangulation(*t2))

    t3 = [1,3,1,4,1,5],
    print(sol.minScoreTriangulation(*t3))