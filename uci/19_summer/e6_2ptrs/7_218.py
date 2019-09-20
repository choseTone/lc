__author__ = 'wangqc'

# https://leetcode.com/problems/the-skyline-problem/


import heapq

class Solution:
    def getSkyline(self, buildings):
        bldgs = sorted([(l,-h,r) for l,r,h in buildings] + list({(r,0,0) for _,r,_ in buildings}))
        points, contour = [[0, 0]], [(0, float("inf"))]
        for l, neg_h, r in bldgs:
            while l >= contour[0][1]:
                heapq.heappop(contour)
            if neg_h:
                heapq.heappush(contour, (neg_h, r))
            if points[-1][1] + contour[0][0]:
                points.append([l, -contour[0][0]])
        return points[1:]


if __name__ == '__main__':
    sol = Solution()

    t1 = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]],
    print(sol.getSkyline(*t1))

    t2 = [[1,2,1],[1,2,2],[1,2,3]],
    print(sol.getSkyline(*t2))