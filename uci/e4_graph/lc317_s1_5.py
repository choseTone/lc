__author__ = 'wangqc'

# https://leetcode.com/problems/maximum-vacation-days/discuss/212355/Python-Graph-and-DP

def maxVacationDays(flights, days):
	n, k = len(days), len(days[0])
	g = [[j for j, dst in enumerate(city) if dst]+[i] for i, city in enumerate(flights)]
	dp = [[0] * n for _ in range(k+1)]
	for w in range(k)[::-1]:
		for c in range(n):
			dp[w][c] = days[c][w] + max(dp[w+1][dst] for dst in g[c])
	return max(dp[0][dst] for dst in g[0])