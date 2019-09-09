__author__ = 'wangqc'

# https://leetcode.com/problems/profitable-schemes/


class Solution:
    def profitableSchemes(self, G, P, group, profit):
        M = 10**9 + 7
        dp = [[1]+[0]*G] + [[0]*(G+1) for _ in range(P)]
        for g, p in zip(group, profit):
            for i in range(P,-1,-1):
                for j in range(G-g,-1,-1):
                    x, y = min(P, i+p), j+g
                    dp[x][y] = (dp[x][y] + dp[i][j]) % M
        return sum(dp[P]) % M


if __name__ == '__main__':
    sol = Solution()

    t1 = 5, 3, [2,2], [2,3],
    print(sol.profitableSchemes(*t1))

    t2 = 10, 5, [2,3,5],[6,7,8],
    print(sol.profitableSchemes(*t2))