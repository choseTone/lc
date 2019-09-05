__author__ = 'wangqc'

# https://leetcode.com/problems/dungeon-game/


class Solution:
    def calculateMinimumHP(self, dungeon):
        #   dp[i][j] = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
        M, N = len(dungeon), len(dungeon[0])
        dp = [[0]*N + [float('inf')] for _ in range(M)] + [[float('inf')]*(N-1)+[1,333]]
        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
        return dp[0][0]


if __name__ == '__main__':
    sol = Solution()

    t1 = [
             [-2, -3, 3],
             [-5,-10, 1],
             [10, 30,-5]
         ],
    print(sol.calculateMinimumHP(*t1))