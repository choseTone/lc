__author__ = 'wangqc'

# https://leetcode.com/problems/find-the-shortest-superstring/

from itertools import combinations

class Solution:
    def shortestSuperstring(self, A):
        def merge(a, b):
            for i in range(len(b)+1)[::-1]:
                if a.endswith(b[:i]):
                    return i

        def dfs(sup, s, st):
            self.sss = min(self.sss, sup+''.join(st), key=len)
            if st and any(right in st for right in merged[s][1:]):
                for right in merged[s][1:]:
                    if right in st:
                        dfs(sup+right[merged[s][0]:], right, st-{right})
            else:
                for new in st:
                    for right in merged[new][1:]:
                        if right in st:
                            dfs(sup + new + right[merged[new][0]:], right, st-{new, right})

        merged, self.sss = {}, ''.join(A)
        for a, b in combinations(A, 2):
            for a, b in ((a, b), (b, a)):
                l = merge(a, b)
                if a not in merged or l > merged[a][0]:
                    merged[a] = [l, b]
                elif l == merged[a][0]:
                    merged[a].append(b)
        for a in A:
            dfs(a, a, set(A) - {a})
        return self.sss


if __name__ == '__main__':
    sol = Solution()

    t1 = ["alex","loves","leetcode"],
    print(sol.shortestSuperstring(*t1))

    t2 = ["catg","ctaagt","gcta","ttca","atgcatc"],
    print(sol.shortestSuperstring(*t2))