__author__ = 'wangqc'

'''
123. Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
             
Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
             
Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''


class Solution:
    # use dp to update two lists, prev and cur, storing the largest value achieved at index i
    # cur[i] profit is added on prev[i], indicates cur transaction's profit is built on prev transaction
    # update dp(prev and cur) 2 times means i can make 2 transactions: add my profit on 1 previous transactions
    def maxProfit(self, prices):
        if not prices: return 0
        n = len(prices)
        cur = [0] * n
        for _ in range(2):
            prev, val = cur[:], cur[0] - prices[0]
            for i in range(1, n):
                cur[i] = max(cur[i - 1], val + prices[i])
                val = max(val, prev[i] - prices[i])
        return cur[n-1]


if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.maxProfit([3,3,5,0,0,3,1,4])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))