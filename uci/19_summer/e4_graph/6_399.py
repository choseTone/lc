__author__ = 'wangqc'

# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/


class Solution:
    def calcEquation(self, equations, values, queries):
        root = {}

        # xr = x/parent(x), pr = parent(x)/root(x), update xr to xr*pr = x/root(x)
        def find(x):
            p, xr = root.setdefault(x, (x, 1.0))
            if x != p:
                r, pr = find(p)
                root[x] = (r, xr*pr)
            return root[x]

        # if root(x) = root(y), equations "x / y" doable as (x/root(x)) / (y/root(y)) = xr / yr
        def union(x, y, load):
            px, xr, py, yr = *find(x), *find(y)
            if not load:
                return xr / yr if px == py else -1.0
            if px != py:
                root[px] = (py, yr/xr*load)

        for (x, y), v in zip(equations, values):
            union(x, y, v)
        return [union(x, y, 0) if x in root and y in root else -1.0 for x, y in queries]


if __name__ == '__main__':
    sol = Solution()

    t1 = [["a", "b"], ["b", "c"]], \
         [2.0, 3.0], \
         [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
    print(sol.calcEquation(*t1))

    t2 = [["a", "b"], ["e", "f"], ["b", "e"]], \
         [3.4, 1.4, 2.3],\
         [["b", "a"], ["a", "f"], ["f", "f"], ["e", "e"], ["c", "c"], ["a", "c"], ["f", "e"]],
    print(sol.calcEquation(*t2))