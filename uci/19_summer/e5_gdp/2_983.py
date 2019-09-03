__author__ = 'wangqc'

# https://leetcode.com/problems/minimum-cost-for-tickets/


class Solution:
    def mincostTickets(self, days, costs):
        dp, plans, prev = [0] * (days[-1]+1), [1,7,30], 0
        for curr in days:
            dp[prev:curr] = [dp[prev]]*(curr-prev)
            dp[curr] = min(dp[max(0,curr-d)]+p for d,p in zip(plans, costs))
            prev = curr
        return dp[-1]



if __name__ == '__main__':
    sol = Solution()

    t1 = [1,4,6,7,8,20], [2,7,15],
    print(sol.mincostTickets(*t1))

    t2 = [1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15],
    print(sol.mincostTickets(*t2))