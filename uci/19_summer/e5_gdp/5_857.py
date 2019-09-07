__author__ = 'wangqc'

# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/


import heapq

class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        base, cost, projects = 0, float('inf'), []
        for ratio, w, q in sorted(((w/q), w, q) for w, q in zip(wage, quality)):
            base += q
            heapq.heappush(projects, -q)
            if len(projects) > K:
                base += heapq.heappop(projects)
            if len(projects) == K:
                cost = min(cost, ratio*base)
        return cost


if __name__ == '__main__':
    sol = Solution()

    t1 = [10,20,5], [70,50,30], 2,
    print(sol.mincostToHireWorkers(*t1))

    t2 = [3,1,10,10,1], [4,8,2,2,7], 3,
    print(sol.mincostToHireWorkers(*t2))