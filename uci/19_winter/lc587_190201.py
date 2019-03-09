__author__ = 'wangqc'

'''
587. Erect the Fence

There are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden. 
Your job is to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced 
only if all the trees are enclosed. Your task is to help find the coordinates of trees which are exactly located 
on the fence perimeter.

Example 1:
Input: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]

Example 2:
Input: [[1,2],[2,2],[4,2]]
Output: [[1,2],[2,2],[4,2]]
Explanation: Even you only have trees in a line, you need to use rope to enclose them. 
 
Note:
All trees should be enclosed together. You cannot cut the rope to enclose trees that will separate them in more than one group.
All input integers will range from 0 to 100.
The garden has at least one tree.
All coordinates are distinct.
Input points have NO order. No order required for output.
'''


class Solution:
    def outerTrees(self, points):
        if len(points) < 2: return points
        # convex hull: if slope koa < kob, then a is inclusive to ob
        def inclusive(o, a, b):
            return (a[0]-o[0]) * (b[1]-o[1]) - (a[1]-o[1]) * (b[0]-o[0]) < 0
        # scan and exclude all inclusive points so only the outer points stays
        def draw(points, line):
            for p in points:
                while len(line) > 1 and inclusive(line[-2], line[-1], p):
                    line.pop()
                line.append(p)
        points = sorted(points, key=lambda p: (p[0], p[1]))
        lower, upper = [], []
        # scan from left to right and exclude all inclusive points will get the lower outline
        # while scan from right to left will get the upper
        draw(points, lower), draw(points[::-1], upper)
        return list(set(lower[:-1] + upper[:-1]))


if __name__ == '__main__':
    sol = Solution()
    argv = [(1,1),(2,2),(2,0),(2,4),(3,3),(4,2)]
    ans = sol.outerTrees(argv)
    print('Input : %s\nOutput: %s' % (argv, ans))

