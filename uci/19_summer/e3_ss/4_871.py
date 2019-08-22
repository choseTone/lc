__author__ = 'wangqc'


# https://leetcode.com/problems/minimum-number-of-refueling-stops/

import heapq


class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        stock, src, cnt = [], 0, 0
        for dst, fuel in stations + [[target, 0]]:
            startFuel -= dst-src
            while stock and startFuel < 0:
                startFuel -= heapq.heappop(stock)
                cnt += 1
            if startFuel < 0:
                return -1
            src = dst
            heapq.heappush(stock, -fuel)
        return cnt



if __name__ == '__main__':
    sol = Solution()

    t1 = 100, 1, [[10,100]],
    print(sol.minRefuelStops(*t1))

    t2 = 100, 10, [[10,60],[20,30],[30,30],[60,40]],
    print(sol.minRefuelStops(*t2))
