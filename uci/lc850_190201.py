__author__ = 'wangqc'

'''
850. Rectangle Area II

We are given a list of (axis-aligned) rectangles. Each rectangle[i] = [x1, y1, x2, y2] , where (x1, y1) are the 
coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the ith rectangle.
Find the total area covered by all rectangles in the plane.  Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6

Example 2:
Input: [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.

Note:
1 <= rectangles.length <= 200
rectanges[i].length = 4
0 <= rectangles[i][j] <= 10^9
The total area covered by all rectangles will never exceed 2^63 - 1 and thus will fit in a 64-bit signed integer.
'''

import bisect

class Solution:
    def rectangleArea(self, rectangles):
        # sweep one rect out before sweep another rect in if at the same line-y
        IN, OUT = 1, 0
        # sweep from bottom to top. Each time sweep in or out of a rect, update area
        sweep = sorted(node for x1,y1,x2,y2 in rectangles for node in ((y1,IN,x1,x2), (y2,OUT,x1,x2)))
        y0, xs, area = sweep[0][0], [], 0
        # total width of current swept-in rects, could be overlapped or separated
        def get_width():
            w, r = 0, -1
            # linear scan since xs is always sorted
            for x1, x2 in xs:
                r = max(r, x1)
                w += max(0, x2-r)
                r = max(r, x2)
            return w
        for y, status, x1, x2 in sweep:
            area += get_width() * (y-y0)
            if status==IN: bisect.insort(xs, (x1, x2))   # keep xs sorted
            else: xs.remove((x1, x2))
            y0 = y
        return area % (10**9+7)


if __name__ == '__main__':
    sol = Solution()
    argv = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
    ans = sol.rectangleArea(argv)
    print('Input : %s\nOutput: %s' % (argv, ans))

