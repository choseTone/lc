__author__ = 'wangqc'

# https://leetcode.com/problems/rectangle-area-ii/

import bisect


class Solution:
    def rectangleArea(self, rectangles):
        IN, OUT, M = 1, 0, 10**9 + 7
        plane = sorted(node for x1,y1,x2,y2 in rectangles for node in ((y1,IN,x1,x2), (y2,OUT,x1,x2)))
        y0, xs, area = plane[0][0], [], 0

        def get_width():
            w, r = 0, -1
            for x1, x2 in xs:
                r = max(r, x1)
                w += max(0, x2-r)
                r = max(r, x2)
            return w

        for y, status, x1, x2 in plane:
            area = (area + get_width() * (y - y0)) % M
            if status:
                bisect.insort(xs, (x1, x2))
            else:
                xs.remove((x1, x2))
            y0 = y
        return area


if __name__ == '__main__':
    sol = Solution()

    t1 = [[0,0,2,2],[1,0,2,3],[1,0,3,1]],
    print(sol.rectangleArea(*t1))

    t2 = [[0,0,1000000000,1000000000]],
    print(sol.rectangleArea(*t2))