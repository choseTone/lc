__author__ = 'wangqc'

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/


class Solution:
    def maxProfit(self, K, prices):
        N = len(prices)
        if K > N >> 1:
            return sum(prices[i+1]-prices[i] for i in range(N-1) if prices[i+1]>prices[i])

        cash, asset = [float('-inf')]*(K+1), [0]*(K+1)
        for price in prices:
            for k in range(1,K+1):
                asset[k] = max(asset[k], cash[k] + price)
                cash[k] = max(cash[k], asset[k-1] - price)
        return asset[K]


if __name__ == '__main__':
    sol = Solution()

    t1 = 2, [2,4,1],
    print(sol.maxProfit(*t1))

    t2 = 2, [3,2,6,5,0,3],
    print(sol.maxProfit(*t2))