__author__ = 'wangqc'

'''
121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design 
an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''


class Solution:
    def maxProfit(self, prices):
        b, ans = float('inf'), 0
        for p in prices:
            b, ans = min(b, p), max(ans, p - b)
        return ans


if __name__ == '__main__':
    from time import time
    from random import randint

    sol = Solution()
    t = time()
    prices = [randint(1, 100) for _ in range(20)]
    ans = sol.maxProfit(prices)
    # prices: [16, 68, 27, 55, 25, 78, 35, 39, 9, 34, 28, 75, 62, 31, 59, 20, 14, 3, 66, 51]	ans: 66
    print('prices: %s\tans: %d\ntime: %.3fms' % (prices, ans, ((time() - t)) * 1000))