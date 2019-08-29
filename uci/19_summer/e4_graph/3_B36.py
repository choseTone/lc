__author__ = 'wangqc'

# https://leetcode.com/problems/parallel-courses/

from collections import defaultdict

class Solution:
    def minimumSemesters(self, N, relations):
        src, dst = defaultdict(set), defaultdict(set)
        for s, d in relations:
            src[d].add(s)
            dst[s].add(d)
        q = [(x, 1) for x in range(1, N+1) if not src[x]]
        for node, sem in q:
            for nei in dst[node]:
                src[nei].remove(node)
                if not src[nei]:
                    q.append((nei, sem+1))
        return q[-1][1] if len(q) == N else -1


if __name__ == '__main__':
    sol = Solution()

    t1 = 3, [[1,3],[2,3]],
    print(sol.minimumSemesters(*t1))
