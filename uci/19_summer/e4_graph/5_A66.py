__author__ = 'wangqc'

# https://leetcode.com/problems/campus-bikes-ii/

import heapq


class Solution:
    def assignBikes(self, workers, bikes):
        def d(x, y):
            return sum(abs(workers[x][i]-bikes[y][i]) for i in (0,1))

        pq, seen, M, N = [(0, 0, 0)], set(), len(workers), len(bikes)
        while pq:
            cost, worker, bikes_taken = heapq.heappop(pq)
            if worker == M:
                return cost
            if (worker, bikes_taken) not in seen:
                seen.add((worker, bikes_taken))
                for bike in range(N):
                    if not bikes_taken & (1<<bike):
                        heapq.heappush(pq, (cost+d(worker,bike), worker+1, bikes_taken|(1<<bike)))


if __name__ == '__main__':
    sol = Solution()

    t1 = [[0,0],[2,1]], [[1,2],[3,3]],
    print(sol.assignBikes(*t1))

    t2 = [[239,904],[191,103],[260,117],[86,78],[747,62]], \
         [[660,8],[431,772],[78,576],[894,481],[451,730],[155,28]],
    print(sol.assignBikes(*t2))
