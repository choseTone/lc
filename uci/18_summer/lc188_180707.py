__author__ = 'wangqc'

'''
188. Best Time to Buy and Sell Stock IV

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:
Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
'''


class Solution:
    # when k > len(prices) / 2, case equals to unlimited times of transactions
    # use dp to update two lists, prev and cur, storing the largest value achieved at index i
    # cur[i] profit is added on prev[i], indicates cur transaction's profit is built on prev transaction
    # update dp(prev and cur) k times means i can make k transactions: add my profit on 1 previous transactions
    def maxProfit(self, k, prices):
        if not prices: return 0
        n = len(prices)
        if k > n >> 1:
            ans = 0
            for j in range(n - 1):
                ans += max(0, prices[j + 1] - prices[j])
            return ans
        cur = [0] * n
        for _ in range(k):
            prev, val = cur[:], cur[0] - prices[0]
            for i in range(1, n):
                cur[i] = max(cur[i - 1], val + prices[i])
                val = max(val, prev[i] - prices[i])
        return cur[n-1]


if __name__ == '__main__':
    from time import time
    from random import randint

    sol = Solution()
    t = time()
    prices, k = [randint(1, 20) for _ in range(50)], 7
    ans = sol.maxProfit(k, prices)
    print('prices: %s\tk: %d\nans: %s\ntime: %.3fms' % (prices, k, ans, ((time() - t)) * 1000))