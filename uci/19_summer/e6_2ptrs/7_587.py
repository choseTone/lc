__author__ = 'wangqc'

# https://leetcode.com/problems/erect-the-fence/


class Solution:
    def outerTrees(self, points):
        if len(points) < 2:
            return points

        def inclusive(o, x, y):
            return (x[0]-o[0]) * (y[1]-o[1]) < (x[1]-o[1]) * (y[0]-o[0])

        def draw(points):
            line = []
            for p in points:
                while len(line) > 1 and inclusive(line[-2], line[-1], p):
                    line.pop()
                line.append(p)
            return line[::-1]

        points = sorted((x, y) for x, y in points)
        return [[x, y] for x, y in set(draw(points) + draw(points[::-1]))]


if __name__ == '__main__':
    sol = Solution()

    t1 = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]],
    print(sol.outerTrees(*t1))

    t2 = [[1,2],[2,2],[4,2]],
    print(sol.outerTrees(*t2))

    t3 = [[0,0],[0,100],[100,100],[100,0],[50,50]],
    print(sol.outerTrees(*t3))