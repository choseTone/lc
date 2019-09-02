__author__ = 'wangqc'

# https://leetcode.com/problems/coin-change/


class Solution:
    def coinChangeDP(self, coins, amount):
        dp = [0]
        for x in range(1, amount+1):
            dp.append(min((dp[x-coin]+1 for coin in coins if coin <= x and dp[x-coin]>=0), default=-1))
        return dp[amount]

    # DFS works better if amount is huge, could be O(c**n)
    def coinChangeDFS(self, coins, amount):
        coins.sort(reverse=True)
        N, self.min = len(coins), float("inf")

        def dfs(undo, cnt, i):
            if not undo:
                self.min = min(self.min, cnt)
            for j in range(i, N):
                if coins[j] <= undo < coins[j]*(self.min-cnt):
                    dfs(undo-coins[j], cnt+1, j)

        for i in range(N):
            dfs(amount, 0, i)
        return self.min if self.min < float("inf") else -1



if __name__ == '__main__':
    sol = Solution()

    t1 = [1,2,5], 11,
    print(sol.coinChangeDP(*t1))
    print(sol.coinChangeDFS(*t1))

    t2 = [2], 3,
    print(sol.coinChangeDP(*t2))
    print(sol.coinChangeDFS(*t2))