__author__ = 'wangqc'

# https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations):
        p, sz = list(range(26)), [0]*26

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if sz[px] < sz[py]:
                    px, py = py, px
                p[py], sz[px] = px, sz[px] + 1

        eqs, neqs = [], []
        for a, op, _, b in equations:
            if op == "=":
                eqs.append((ord(a)-97, ord(b)-97))
            else:
                neqs.append((ord(a)-97, ord(b)-97))
        for a, b in eqs:
            union(a, b)
        return all(find(a) != find(b) for a, b in neqs)


if __name__ == '__main__':
    sol = Solution()

    t1 = ["a==b","b==c","a==c"],
    print(sol.equationsPossible(*t1))

    t2 = ["a==b","b!=c","c==a"],
    print(sol.equationsPossible(*t2))

    t3 = ["c==c","b==d","x!=z"],
    print(sol.equationsPossible(*t3))