__author__ = 'wangqc'

# https://leetcode.com/problems/ipo/


import heapq

class Solution:
    def findMaximizedCapital(self, k, W, Profits, Capital):
        pq, projects = [], sorted(zip(Capital, Profits))
        i, N = 0, len(projects)
        for _ in range(k):
            while i < N and W >= projects[i][0]:
                heapq.heappush(pq, -projects[i][1])
                i += 1
            if pq:
                W -= heapq.heappop(pq)
            else:
                break
        return W


if __name__ == '__main__':
    sol = Solution()

    t1 = 2, 0, [1,2,3], [0,1,1],
    print(sol.findMaximizedCapital(*t1))