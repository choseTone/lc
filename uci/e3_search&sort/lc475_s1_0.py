__author__ = 'wangqc'

# https://leetcode.com/problems/heaters/discuss/258260/Python-Binary-Search

import bisect

def findRadius(houses, heaters):
	heaters = [float('-inf')] + sorted(heaters) + [float('inf')]
	return max(min(abs(house-heater) for heater in heaters[i-1:i+1]) for house in houses for i in [bisect.bisect(heaters, house)])