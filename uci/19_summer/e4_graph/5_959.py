__author__ = 'wangqc'

# https://leetcode.com/problems/regions-cut-by-slashes/


class Solution:
    def regionsBySlashes(self, grid):
        N = len(grid)
        p, sz = list(range(N*N<<2)), [0]*(N*N<<2)

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if sz[px] < sz[py]:
                    px, py = py, px
                p[py] = px
                sz[px] += 1

        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                o = i*N+j<<2
                # |\0/|\4/|
                # |1X2|5X6|
                # |/3\|/7\|
                if c in "/ ":
                    union(o, o+1), union(o+2,o+3)
                if c in "\ ":
                    union(o, o+2), union(o+1, o+3)
                if i < N-1:
                    union(o+3, o+(N<<2))
                if j < N-1:
                    union(o+2, o+5)
        return sum(find(x)==x for x in set(p))


if __name__ == '__main__':
    sol = Solution()

    t1 = [
             " /",
             "/ "
         ],
    print(sol.regionsBySlashes(*t1))

    t2 = [
             "\\/",
             "/\\"
         ],
    print(sol.regionsBySlashes(*t2))

    t3 = [
             "/\\",
             "\\/"
         ],
    print(sol.regionsBySlashes(*t3))

    t4 = [
             "//",
             "/ "
         ],
    print(sol.regionsBySlashes(*t4))
